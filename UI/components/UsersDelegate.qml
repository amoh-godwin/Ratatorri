import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import Qt.labs.qmlmodels 1.0


DelegateChooser {

    DelegateChoice {
        column: 0
        delegate: Text {
            text: model.display
        }
    }

    DelegateChoice {
        column: 1
        delegate: Text {
            text: model.display
        }
    }

    DelegateChoice {
        column: 12
        delegate: Text {
            text: model.display
        }
    }

}

