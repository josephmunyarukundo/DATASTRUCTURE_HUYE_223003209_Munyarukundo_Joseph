#include <iostream>
#include <cstring> // for strcpy, strcmp

struct State {
    char color[10];
    int duration;
};

class TrafficLightController {
protected:
    State* states;   // dynamic array of states
    int numStates;
    int currentState;

public:
    TrafficLightController(State* states_, int n) : numStates(n), currentState(0) {
        states = new State[numStates];
        for(int i=0; i<numStates; i++) {
            states[i] = states_[i];
        }
    }

    virtual ~TrafficLightController() {
        delete[] states;
    }

    virtual void cycleStates() = 0; // pure virtual
};

class SimpleController : public TrafficLightController {
public:
    SimpleController(State* s, int n) : TrafficLightController(s,n) {}

    void cycleStates() override {
        State* ptr = states + currentState;
        std::cout << "SimpleController: Light is " << ptr->color 
                  << " for " << ptr->duration << " seconds.\n";
        currentState = (currentState + 1) % numStates;
    }
};

class PedestrianController : public TrafficLightController {
public:
    PedestrianController(State* s, int n) : TrafficLightController(s,n) {}

    void cycleStates() override {
        State* ptr = states + currentState;
        std::cout << "PedestrianController: Signal " << ptr->color 
                  << " for " << ptr->duration << " seconds.\n";
        currentState = (currentState + 1) % numStates;
    }
};

class ControllerManager {
    TrafficLightController** controllers;
    int count;
public:
    ControllerManager() : controllers(nullptr), count(0) {}

    ~ControllerManager() {
        for(int i=0; i<count; i++) {
            delete controllers[i];
        }
        delete[] controllers;
    }

    void addController(TrafficLightController* ctrl) {
        TrafficLightController** temp = new TrafficLightController*[count + 1];
        for(int i=0; i<count; i++) {
            temp[i] = controllers[i];
        }
        temp[count] = ctrl;
        delete[] controllers;
        controllers = temp;
        count++;
    }

    void removeController(int index) {
        if(index < 0 || index >= count) return;
        delete controllers[index];
        TrafficLightController** temp = new TrafficLightController*[count - 1];
        for(int i=0, j=0; i<count; i++) {
            if(i!=index) {
                temp[j++] = controllers[i];
            }
        }
        delete[] controllers;
        controllers = temp;
        count--;
    }

    void cycleAll() {
        for(int i=0; i<count; i++) {
            controllers[i]->cycleStates();
        }
    }
};

int main() {
    State simpleStates[] = { {"Red", 10}, {"Green", 15}, {"Yellow", 5} };
    State pedestrianStates[] = { {"Walk", 10}, {"Don'tWalk", 20} }; 

    ControllerManager manager;

    manager.addController(new SimpleController(simpleStates, 3));
    manager.addController(new PedestrianController(pedestrianStates, 2));

    std::cout << "Cycling states 5 times:\n";
    for(int i=0; i<5; i++) {
        manager.cycleAll();
        std::cout << "---\n";
    }

    // Remove first controller (SimpleController)
    manager.removeController(0);

    std::cout << "After removing first controller:\n";
    for(int i=0; i<3; i++) {
        manager.cycleAll();
        std::cout << "---\n";
    }

    return 0;
}
