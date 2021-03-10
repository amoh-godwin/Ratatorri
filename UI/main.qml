import QtQuick 2.15
import QtQuick.Controls 2.15
import "components" as Comps

ApplicationWindow {
    visible: true
    width: 480
    height: 560
    title: "Ratatorri"

    StackView {
        id: stack
        anchors.fill: parent
        initialItem: welcComp

    }

    Comps.WelcomeComp { id: welcComp; }
    Comps.UsersComp { id: userComp; }

}
