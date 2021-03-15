import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Component {

    Rectangle {
        width: parent.width
        height: 36

        RowLayout {
            anchors.fill: parent

            Text {
                text: email
            }

            Text {
                text: status
            }

        }

    }

}
