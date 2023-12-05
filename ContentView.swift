import SwiftUI
@main
struct BillRouletteApp: App {
    var userSession = UserSession()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(userSession)
        }
    }
}

struct ContentView: View {
    @EnvironmentObject var userSession: UserSession

    var body: some View {
        if userSession.isSignedIn {
            MainTabView()
        } else {
            SignUpView()
        }
    }
}

struct SignUpView: View {
    @EnvironmentObject var userSession: UserSession

    var body: some View {
        VStack {
            Text("Welcome to Bill Roulette")
                .font(.largeTitle)
                .padding()

            Button("Play Now") {
                userSession.signIn()
            }
            .buttonStyle(CustomButtonStyle())
        }
    }
}

struct CustomButtonStyle: ButtonStyle {
    func makeBody(configuration: Self.Configuration) -> some View {
        configuration.label
            .padding()
            .background(Color.blue)
            .foregroundColor(.white)
            .clipShape(RoundedRectangle(cornerRadius: 10))
            .scaleEffect(configuration.isPressed ? 0.9 : 1.0)
    }
}

struct MainTabView: View {
    @EnvironmentObject var userSession: UserSession

    var body: some View {
        TabView {
            BillRouletteView()
                .tabItem {
                    Label("Roulette", systemImage: "circle")
                }

            InformationView()
                .tabItem {
                    Label("Info", systemImage: "info.circle")
                }
                .environmentObject(userSession)
        }
    }
}

struct BillRouletteView: View {
    @State private var names: [String] = []
    @State private var currentName: String = ""
    @State private var selectedName: String = ""
    @State private var isWheelSpinning = false
    @State private var wheelAngle = 0.0
    @EnvironmentObject var userSession: UserSession
    @State private var displayIndex = 0

    var body: some View {
        VStack {
            TextField("Enter name", text: $currentName)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()

            Button("Add Name") {
                addName()
            }
            .buttonStyle(CustomButtonStyle())
            .disabled(currentName.isEmpty)

            ZStack {
                Circle()
                    .stroke(lineWidth: 5)
                    .foregroundColor(.blue)
                    .frame(width: 200, height: 200)

                if isWheelSpinning {
                    Text(names[displayIndex])
                        .font(.title)
                        .transition(.opacity)
                        .id(displayIndex)
                } else {
                    Text(selectedName)
                        .font(.title)
                }
            }
            .padding()

            Button("Whose Paying!") {
                spinWheel()
            }
            .buttonStyle(CustomButtonStyle())
            .disabled(names.isEmpty)

            Spacer()

            Button("Back") {
                userSession.signOut()
            }
            .buttonStyle(CustomButtonStyle())
        }
    }

    func addName() {
        names.append(currentName)
        currentName = ""
    }

    func deleteName(at offsets: IndexSet) {
        names.remove(atOffsets: offsets)
    }

    func spinWheel() {
        guard !names.isEmpty else { return }
        isWheelSpinning = true
        let randomTurns = Int.random(in: 5...10)
        let totalDuration = Double(randomTurns)
        let timePerName = totalDuration / Double(names.count * randomTurns)

        Timer.scheduledTimer(withTimeInterval: timePerName, repeats: true) { timer in
            displayIndex = (displayIndex + 1) % names.count

            if !isWheelSpinning {
                timer.invalidate()
            }
        }

        DispatchQueue.main.asyncAfter(deadline: .now() + totalDuration) {
            selectRandomName()
            isWheelSpinning = false
        }
    }

    func selectRandomName() {
        guard let name = names.randomElement() else { return }
        selectedName = name
        userSession.addPayer(name)
    }
}

struct InformationView: View {
    @EnvironmentObject var userSession: UserSession

    var body: some View {
        VStack {
            Text("Past Bill Payers")
                .font(.headline)
                .padding()

            List(userSession.pastPayers, id: \.self) { payer in
                Text(payer)
            }
        }
    }
}

class UserSession: ObservableObject {
    @Published var isSignedIn = false
    @Published var pastPayers: [String] = []

    func signIn() {
        isSignedIn = true
    }

    func signOut() {
        isSignedIn = false
    }

    func addPayer(_ name: String) {
        pastPayers.append(name)
    }
}

struct ContentView_Previews:           PreviewProvider {
    static var previews: some View {
        ContentView().environmentObject(UserSession())
    }
}
