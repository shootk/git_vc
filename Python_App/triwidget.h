class QWidget;
class QMenu;
class QAction;

class TrayWidget : public QSystemTrayIcon {
 Q_OBJECT
 public:
  explicit TrayWidget(QWidget *parent = Q_NULLPTR);

 private:
  QMenu *menu_;
  QAction *action_quit_;
  QAction *action_qt_;

 public Q_SLOTS:
  void Message();
};