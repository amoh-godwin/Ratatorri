import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import Qt.labs.qmlmodels 1.0


DelegateChooser {

    DelegateChoice {
        column: 0
        delegate: Text {
            text: model.display

            Component.onCompleted: one = this.width

        }
    }

    DelegateChoice {
        column: 1
        delegate: TextField {
            text: model.display
            selectByMouse: true
        }
    }

    DelegateChoice {
        column: 2
        delegate: TextField {
            text: model.display
            selectByMouse: true

            Component.onCompleted: four = this.width

        }
    }

    DelegateChoice {
        column: 5
        delegate: Text {
            text: model.display

            Component.onCompleted: twelve = this.width

        }
    }

}

