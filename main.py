from view.main_view import MainView
from presenter.main_presenter import MainPresenter

if __name__ == "__main__":
    presenter = MainPresenter(None)
    app = MainView(presenter)
    presenter.view = app
    app.mainloop()
