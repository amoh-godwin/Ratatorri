import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Component {

    Rectangle {

        ScrollView {
            anchors.fill: parent

            ListView {
                id: listview
                model: UsersBaseModel {}
                delegate: UsersDelegate {}
            }
        }

    }

}
