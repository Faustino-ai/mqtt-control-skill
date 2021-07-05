from mycroft import MycroftSkill, intent_file_handler


class MqttControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.mqtt.intent')
    def handle_control_mqtt(self, message):
        self.speak_dialog('control.mqtt')


def create_skill():
    return MqttControl()

