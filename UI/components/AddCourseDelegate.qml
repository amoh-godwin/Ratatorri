import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Component {

    Rectangle {
        width: parent.width
        height: 36

        RowLayout {
            anchors.fill: parent
            anchors.margins: 8

            Text {
                Layout.fillWidth: true
                text: email
            }

            Text {
                Layout.preferredWidth: 72
                text: status
                color: text == 'success' ? "green": "gold"
            }

        }

    }

}
