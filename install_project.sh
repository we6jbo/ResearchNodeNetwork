#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="${HOME}/Projects/ResearchNodeNetwork"
SHARE_DIR="${HOME}/.local/share/research-node-network"
BIN_DIR="${HOME}/.local/bin"
SYSTEMD_DIR="${HOME}/.config/systemd/user"
BUILD_DIR="${PROJECT_ROOT}/build"

if [[ ! -d "$PROJECT_ROOT" ]]; then
  echo "STOP: $PROJECT_ROOT does not exist."
  echo "Create ResearchNodeNetwork in Qt Creator first, then run the outer installer again."
  exit 2
fi

for pkg in cmake ninja qt6-base python; do
  if ! pacman -Q "$pkg" >/dev/null 2>&1; then
    echo "Missing Manjaro/Arch package: $pkg"
    echo "Install official repository dependencies with:"
    echo "  sudo pacman -S --needed cmake ninja qt6-base python"
    exit 3
  fi
done

echo "Current system time:"
date --iso-8601=seconds || date

# Detect files whose timestamps are materially in the future.
FUTURE_FILES="$(find "$PROJECT_ROOT" -path "$BUILD_DIR" -prune -o -type f -newermt 'now + 5 seconds' -print 2>/dev/null || true)"
if [[ -n "$FUTURE_FILES" ]]; then
  echo "Found project files timestamped in the future. Normalizing project timestamps:"
  printf '%s\n' "$FUTURE_FILES"
fi

# Normalize timestamps on source/package content after ZIP extraction.
# Exclude any old build tree because it will be deleted immediately.
find "$PROJECT_ROOT" -path "$BUILD_DIR" -prune -o -type f -exec touch {} +
find "$PROJECT_ROOT" -path "$BUILD_DIR" -prune -o -type d -exec touch {} + 2>/dev/null || true

rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

mkdir -p "$SHARE_DIR" "$BIN_DIR" "$SYSTEMD_DIR" "$HOME/.local/state/research-node-network"

cp -a "$PROJECT_ROOT/data" "$SHARE_DIR/"
cp "$PROJECT_ROOT/tg_context_snapshot.json" "$SHARE_DIR/"
cp "$PROJECT_ROOT/AGENTS.md" "$SHARE_DIR/"
cp "$PROJECT_ROOT/tools/network_agent.py" "$SHARE_DIR/network_agent.py"
chmod +x "$SHARE_DIR/network_agent.py"

cat > "$BIN_DIR/research-node-network-agent" <<EOF
#!/usr/bin/env bash
export RNN_SHARE_DIR="$SHARE_DIR"
exec python3 "$SHARE_DIR/network_agent.py" "\$@"
EOF
chmod +x "$BIN_DIR/research-node-network-agent"

# Install the explicit Vibe launcher.
install -m 0755 "$PROJECT_ROOT/vibe/vibe-rnn" "$BIN_DIR/vibe-rnn"

# Merge, never overwrite, the ResearchNodeNetwork bootstrap into Vibe's user AGENTS.md.
RNN_PROJECT_ROOT="$PROJECT_ROOT" python3 "$PROJECT_ROOT/tools/install_vibe_bootstrap.py"

# Verify publication policy before building/installing.
python3 "$PROJECT_ROOT/tools/check_publication_safety.py"

echo "Configuring fresh CMake build..."
cmake -S "$PROJECT_ROOT" -B "$BUILD_DIR" -G Ninja -DCMAKE_BUILD_TYPE=Release

echo "Building..."
cmake --build "$BUILD_DIR" --parallel "$(nproc)"

if [[ ! -x "$BUILD_DIR/ResearchNodeNetwork" ]]; then
  echo "STOP: Build completed without producing $BUILD_DIR/ResearchNodeNetwork"
  exit 4
fi

install -m 0755 "$BUILD_DIR/ResearchNodeNetwork" "$BIN_DIR/ResearchNodeNetwork"

install -m 0644 "$PROJECT_ROOT/systemd/research-node-network.service" "$SYSTEMD_DIR/"
install -m 0644 "$PROJECT_ROOT/systemd/research-node-network-pi.service" "$SYSTEMD_DIR/"
install -m 0644 "$PROJECT_ROOT/systemd/research-node-network-pi.timer" "$SYSTEMD_DIR/"

if command -v sudo >/dev/null 2>&1; then
  sudo install -d -m 0755 -o "$(id -un)" -g "$(id -gn)" /opt/chatgpt/ResearchNodeNetwork || true
fi

if command -v tg-register-project >/dev/null 2>&1; then
  tg-register-project \
    --project-id research-node-network \
    --project-root "$PROJECT_ROOT" \
    --codes "TG918273,TG856134,TG673245,TG749502,TG286753,TG270541,TG307645,TG472690" \
    --reference "ResearchNodeNetwork portable registry graph" || true
fi

systemctl --user daemon-reload
systemctl --user enable --now research-node-network.service
systemctl --user enable --now research-node-network-pi.timer

echo
echo "ResearchNodeNetwork v0.10 installed."
echo "Binary:     $BIN_DIR/ResearchNodeNetwork"
echo "Start node: $("$BIN_DIR/research-node-network-agent" choose-start)"
echo "Service:    systemctl --user status research-node-network.service --no-pager"
echo "Pi timer:   systemctl --user status research-node-network-pi.timer --no-pager"
echo "Traversal:  research-node-network-agent traverse"
