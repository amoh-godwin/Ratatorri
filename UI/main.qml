import QtQuick 2.15
import QtQuick.Controls 2.15
import "components" as Comps

ApplicationWindow {
    visible: true
    width: 1000
    height: 600
    title: "Ratatorri"

    property QtObject backend
    property string users_model: '[{}]'

    // TableView column widths
    property int one: 48 //90
    property int two: 24
    property int three: 24
    property int four: 24
    property int five: 24
    property int six: 24
    property int seven: 24
    property int eight: 24
    property int nine: 24
    property int ten: 24
    property int eleven: 24
    property int twelve: 24

    StackView {
        id: stack
        anchors.fill: parent
        initialItem: welcComp

    }

    Comps.WelcomeComp { id: welcComp; }
    Comps.UsersComp { id: userComp; }
    Comps.AddCourseComp {id: addCourseComp; }
    Comps.WatcherComp {id: watchersComp; }

    Connections {
        target: backend

        function onUsersFetched(users) {
            //users_model = users
            stack.currentItem.modelUpdated(users)
        }

        function onNroll_name(lists) {
            stack.currentItem.addedNames(lists)
        }

        function onNroll_status(ind, status) {
            stack.currentItem.changeStatus(ind, status)
        }

        function onWatchers_nam(lists) {
            stack.currentItem.addedNames(lists)
        }

        function onWatchers_per(ind, per) {
            stack.currentItem.changePercent(ind, per)
        }

    }

}
