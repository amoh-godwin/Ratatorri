import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Component {
    Rectangle {

        signal changePercent(int ind, int per)
        signal addedNames(var names)

        onChangePercent: {
            list_view.model.setProperty(ind, 'percent', per)
        }
        onAddedNames: {
            for (var i=0; i<names.length-1; i++)
                list_view.model.append(names[i])
        }

        StackView.onActivating: backend.watch('Practical Project in Python: Build a Sign in Page')

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
                        model: WatchersBaseModel {}
                        delegate: WatchersDelegate {}
                    }

                }

            }

        }

    }
}
