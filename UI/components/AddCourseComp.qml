import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Component {
    Rectangle {

        signal changeStatus(int ind, string status)
        signal addedNames(var names)

        onChangeStatus: {
            list_view.model.setProperty(ind, 'status', status)
        }
        onAddedNames: {
            for (var i=0; i<names.length-1; i++)
                list_view.model.append(names[i])
        }

        StackView.onActivating: backend.start_nroll_cou()

        ColumnLayout {
            anchors.fill: parent
            spacing: 0

            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: 48
            }

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true

                ScrollView {
                    anchors.fill: parent

                    ListView {
                        id: list_view
                        model: AddCourseBaseModel {}
                        delegate: AddCourseDelegate {}
                    }

                }

            }

        }

    }
}
