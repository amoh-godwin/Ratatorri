import QtQuick 2.15
import Qt.labs.qmlmodels 1.0

TableModel {
    TableModelColumn { display: "fullname" }
    TableModelColumn { display: "email" }
    TableModelColumn { display: "passcode" }
    TableModelColumn { display: "country" }
    TableModelColumn { display: "registered" }
    TableModelColumn { display: "others" }
    TableModelColumn { display: "win_photos" }
    TableModelColumn { display: "python_gui" }
    TableModelColumn { display: "py_gui_ufb" }
    TableModelColumn { display: "pyqt" }
    TableModelColumn { display: "toda" }
    TableModelColumn { display: "soft_dev" }
    TableModelColumn { display: "last_visited" }
    TableModelColumn { display: "python_proj_py" }

    rows: [
        /*{
            fullname: "Hello",
            email: "Hi",
            passcode: "",
            country: "Hello",
            registered: "Hi",
            others: "",
            win_photos: "Hello",
            python_gui: "Hi",
            py_gui_ufb: "",
            pyqt: "Hello",
            toda: "Hi",
            soft_dev: "",
            last_visited: "12"
        }*/
    ]
}
