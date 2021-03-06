import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "../customs" as Custs

Component {

    Rectangle {

        GridLayout {
            width: 248
            height: 128
            anchors.centerIn: parent
            columns: 2

            Custs.CustomButton{
                text: "Users"

                onClicked: stack.push(userComp);

            }

            Custs.CustomButton{
                text: "ADD course"

                onClicked: stack.push(addCourseComp);
            }

            Custs.CustomButton{
                text: "Watchers"

                onClicked: stack.push(watchersComp);
            }

            Custs.CustomButton{
                text: "Hello"
            }


        }

    }

}
