from mididings import *
import threading, time
import subprocess


subprocess.run(["killall", "fluidsynth"])
subprocess.Popen(["fluidsynth", "-a", "alsa", "-m", "alsa_seq", "/home/max/Downloads/Essential Keys-sforzando-v9.6.sf2"])

def checkMidiConnection(): 
    if getMidiDevices() and getSynthDevices() and isSynthActive():
        return True
        return (b"Connected: yes" in subprocess.run(['bluetoothctl', 'info', '14:0E:5E:4E:A6:80'], stdout=subprocess.PIPE).stdout)
    return False

def isSynthActive():
    return (b"fluidsynth" in subprocess.run(["ps", "-A"], stdout=subprocess.PIPE).stdout)


def getMidiDevices():
    midiDevices = []
    for line in subprocess.run(["aconnect", "-l"], stdout=subprocess.PIPE).stdout.splitlines():
        line = line.decode("utf-8")
        if "client" in line:
            if "GZUT-MIDI" in line:
                midiDevices.append(line.split()[1]+"0")
            elif "CHmidi" in line:
                midiDevices.append(line.split()[1]+"0")
    return midiDevices

def getSynthDevices():
    synthDevices = []
    for line in subprocess.run(["aconnect", "-l"], stdout=subprocess.PIPE).stdout.splitlines():
        line = line.decode("utf-8")
        if "FLUID Synth" in line:
            synthDevices.append(line.split()[1]+"0")
    return synthDevices

def getRouterDevices():
    routerDevices = []
    for line in subprocess.run(["aconnect", "-l"], stdout=subprocess.PIPE).stdout.splitlines():
        line = line.decode("utf-8")
        if "MIDIRouter" in line:
            routerDevices.append(line.split()[1]+"0")
    return routerDevices

def autoConnect():
    # wait for Router to startup
    time.sleep(2)
    subprocess.run(["aconnect", "-x"])
    midiDevices = getMidiDevices()
    synthDevices = getSynthDevices()
    routerDevices = getRouterDevices()
    print(f"midiDevices: {midiDevices}")
    print(f"synthDevices: {synthDevices}")
    print(f"routerDevices: {routerDevices}")
    for midiDevice in midiDevices:
        for routerDevice in routerDevices:
            subprocess.run(["aconnect", midiDevice, routerDevice])
            print(f"Connected {midiDevice} to {routerDevice}")
    for routerDevice in routerDevices:
        for synthDevice in synthDevices:
            subprocess.run(["aconnect", routerDevice.replace(":0", ":1"), synthDevice])
            print(f"Connected {routerDevice} to {synthDevice}")
    


def continiousConnect():
    print("Waiting for MIDI devices...")
    while True:
        time.sleep(2)
        if not checkMidiConnection():
            print("MIDI device not found!")
            time.sleep(2)
            continue
        else:
            print("MIDI device found!")
            autoConnect()
            while checkMidiConnection():
                time.sleep(2)
            
# Configuration
config(
    backend='alsa',          # Use 'jack' if running Jack audio
    client_name='MIDIRouter', # Name of the client
)

autoCOnnector = threading.Thread(target=continiousConnect)
autoCOnnector.start()
def adjustVelocity(ev):
    if ev.type == NOTEON:
        velocity = ev.velocity
        print(f"Velocity: {velocity}")
        velocity = 3.34 + 0.306 * velocity + 4.91E-03 * velocity**2
        velocity = int(velocity)
        print(f"Adjusted Velocity: {velocity}")
        ev.velocity = max(0, min(127, velocity))
        
    return ev

hardness = 2/3


def velocityCurveHard(ev):
    if ev.type == NOTEON:
        # 3.34 + 0.306 * velocity + 4.91E-03 * velocity**2
        veolcity = ev.velocity
        velocity = (3.34 + 0.306 * ev.velocity + 4.91E-03 * ev.velocity**2)
        velocity = sum([ev.velocity*(1-hardness), velocity*hardness])
        ev.velocity = int(max(0, min(127, velocity)))
    return ev

run(
    Process(velocityCurveHard)
)