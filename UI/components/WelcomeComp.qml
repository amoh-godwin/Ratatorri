import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "../customs" as Custs

Component {

    Rectangle {
        color: "dodgerblue"

        GridLayout {
            width: 248
            height: 248
            anchors.centerIn: parent
            columns: 2

            Custs.CustomButton{
                text: "Hello"
            }

            Custs.CustomButton{
                text: "Hello"
            }

            Custs.CustomButton{
                text: "Hello"
            }

            Custs.CustomButton{
                text: "Hello"
            }


        }

    }

}
