#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFile>
#include <QStandardPaths>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->statusLabel->setText(
        "Filesystem service interface active.\n"
        "No TCP/UDP listening port is created.\n"
        "Use research-node-network-agent for traversal and exports."
    );
}

MainWindow::~MainWindow()
{
    delete ui;
}
