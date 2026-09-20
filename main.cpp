#include <QApplication>
#include <QCoreApplication>
#include <QDir>
#include <QFile>
#include <QJsonDocument>
#include <QJsonObject>
#include <QProcess>
#include <QStandardPaths>
#include <QTextStream>
#include <QTimer>
#include "mainwindow.h"

// Public/non-secret project provenance identifiers.
// These are intentionally hardwired into the program source.
static constexpr const char *kProjectId = "research-node-network";
static constexpr const char *kTgCodes[] = {
    "TG918273",
    "TG856134",
    "TG673245",
    "TG749502",
    "TG286753",
    "TG270541",
    "TG307645",
    "TG472690"
};
static constexpr int kTgCodeCount = sizeof(kTgCodes) / sizeof(kTgCodes[0]);

static QString joinedTgCodes()
{
    QStringList values;
    for (int i = 0; i < kTgCodeCount; ++i)
        values << QString::fromLatin1(kTgCodes[i]);
    return values.join(',');
}

static QString dataRoot()
{
    const QByteArray env = qgetenv("RNN_DATA_DIR");
    if (!env.isEmpty())
        return QString::fromUtf8(env);
    return QStandardPaths::writableLocation(QStandardPaths::AppLocalDataLocation);
}

static void writeStatus(const QString &mode)
{
    QDir().mkpath(dataRoot());
    QJsonObject o;
    o["project_id"] = QString::fromLatin1(kProjectId);
    o["mode"] = mode;
    o["tg_codes"] = joinedTgCodes();
    o["port_listener"] = false;
    o["transport"] = "filesystem-and-ssh-helper";
    o["service_alive_utc"] = QDateTime::currentDateTimeUtc().toString(Qt::ISODate);
    QFile f(dataRoot() + "/service_status.json");
    if (f.open(QIODevice::WriteOnly | QIODevice::Truncate))
        f.write(QJsonDocument(o).toJson(QJsonDocument::Indented));
}

int main(int argc, char *argv[])
{
    bool serviceMode = false;
    for (int i = 1; i < argc; ++i) {
        if (QString::fromLocal8Bit(argv[i]) == "--service")
            serviceMode = true;
    }

    if (serviceMode) {
        QCoreApplication app(argc, argv);
        QCoreApplication::setApplicationName("ResearchNodeNetwork");
        QCoreApplication::setOrganizationName("j03.page");
        writeStatus("service");
        QTimer timer;
        QObject::connect(&timer, &QTimer::timeout, [](){ writeStatus("service"); });
        timer.start(60000);
        return app.exec();
    }

    QApplication app(argc, argv);
    QCoreApplication::setApplicationName("ResearchNodeNetwork");
    QCoreApplication::setOrganizationName("j03.page");
    writeStatus("gui");
    MainWindow window;
    window.show();
    return app.exec();
}
