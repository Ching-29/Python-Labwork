from model import SalaryReportModel
from view import SalaryReportView
from controller import SalaryReportController


def main():
    model = SalaryReportModel()
    view = SalaryReportView()
    controller = SalaryReportController(model, view)

    controller.run()


if __name__ == "__main__":
    main()
