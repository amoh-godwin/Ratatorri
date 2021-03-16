import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Component {

    Rectangle {
        color: "white"

        signal modelUpdated(var model)

        onModelUpdated: {

            for(var i =0; i<model.length; i++) {
                table_view.model.appendRow(model[i])
            }
        }

        StackView.onActivating: {
            backend.get_users()
        }

        Rectangle {
            anchors.fill: parent
            anchors.margins: 8

            ColumnLayout {
                anchors.fill: parent
                spacing: 8

                Rectangle {
                    Layout.fillWidth: true
                    Layout.preferredHeight: 24

                    RowLayout {
                        //width: parent.width
                        height: parent.height
                        spacing: 0

                        Rectangle {
                            Layout.preferredWidth: one
                            Layout.fillHeight: true
                            Text {
                                text: "Name"
                            }
                        }

                        Rectangle {
                            Layout.preferredWidth: two
                            Layout.fillHeight: true
                            Text {
                                text: "Email"
                            }
                        }

                        Rectangle {
                            Layout.preferredWidth: twelve
                            Layout.fillHeight: true
                            Text {
                                text: twelve//"Last Visited"
                            }
                        }



                    }

                }

                ScrollView {
                    Layout.fillWidth: true
                    Layout.fillHeight: true

                    TableView {
                        id: table_view
                        anchors.fill: parent
                        rowSpacing: 1
                        columnSpacing: 1
                        boundsBehavior: Flickable.StopAtBounds
                        model: UsersBaseModel {}
                        delegate: UsersDelegate {}

                    }
                }

            }

        }

    }

}
