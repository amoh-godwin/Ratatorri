import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Component {

    Rectangle {
        width: 20
        height: 28

        RowLayout {
            Text {
                text: fullname
            }

            Text {
                text: email
            }

        }

    }

}
