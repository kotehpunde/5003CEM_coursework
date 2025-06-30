class Person:
    def __init__(self, username, name, gender, biography="", is_private=False):
        self.username = username
        self.name = name
        self.gender = gender
        self.biography = biography
        self.is_private = is_private
        self.followers = set()
        self.following = set()

    def follow(self, other_person):
        if self.username != other_person.username:
            self.following.add(other_person.username)
            other_person.followers.add(self.username)

    def __str__(self):
        privacy_status = "Private" if self.is_private else "Public"
        return (f"Username: {self.username}\n"
                f"Name: {self.name}\n"
                f"Gender: {self.gender}\n"
                f"Bio: {self.biography}\n"
                f"Privacy: {privacy_status}\n"
                f"Followers: {len(self.followers)} | Following: {len(self.following)}")


class SocialGraph:
    def __init__(self):
        self.users = {}
        self.graph = {}

    def addUser(self, person, silent=False):
        if len(self.users) >= 10:
            if not silent:
                print("User limit reached. Cannot add more than 10 users.")
            return False
        if person.username not in self.users:
            self.users[person.username] = person
            self.graph[person.username] = set()
            if not silent:
                print(f"User '{person.username}' added successfully.")
            return True
        else:
            if not silent:
                print("Username already exists.")
            return False

    def follow(self, follower_username, followee_username):
        if follower_username != followee_username and follower_username in self.graph and followee_username in self.graph:
            self.graph[follower_username].add(followee_username)
            self.users[follower_username].follow(self.users[followee_username])

    def unfollow(self, follower_username, followee_username):
        if (follower_username in self.graph and followee_username in self.graph and
                followee_username in self.graph[follower_username]):
            self.graph[follower_username].remove(followee_username)
            self.users[follower_username].following.discard(followee_username)
            self.users[followee_username].followers.discard(follower_username)

    def getAllUsernames(self):
        return list(self.users.keys())

    def getProfile(self, username):
        return self.users.get(username)

    def getFollowing(self, username):
        return list(self.graph.get(username, []))

    def getFollowers(self, username):
        return [f for f, following in self.graph.items() if username in following]

def setupSampleGraph():
    sg = SocialGraph()
    users = [
        Person("EjenAli", "Ali Abu Bakar", "Male", "Crime Solver", False),
        Person("Beckham7", "David Beckham", "Male", "Footballer", False),
        Person("Joel007", "Joel Vincent", "Male", "Activist", True),
        Person("Johnnyjohnny", "John Cena", "Male", "Wrestler", False),
        Person("MaryKom1", "Mary Kom", "Female", "Boxer", True),
    ]
    for user in users:
        sg.addUser(user, silent=True)

    sg.follow("EjenAli", "Joel007")
    sg.follow("EjenAli", "MaryKom1")
    sg.follow("Joel007", "EjenAli")
    sg.follow("Joel007", "Beckham7")
    sg.follow("MaryKom1", "Johnnyjohnny")
    sg.follow("Beckham7", "Johnnyjohnny")
    sg.follow("Johnnyjohnny", "MaryKom1")

    return sg

# menu
def menu(graph):
    while True:
        print("\n===== Social Media Graph Menu =====")
        print("1. Display all users' names")
        print("2. View a user's profile")
        print("3. View accounts followed by a user")
        print("4. View followers of a user")
        print("5. Exit")
        print("6. Follow a user")
        print("7. Unfollow a user")
        print("8. Add a new user")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            for username in graph.getAllUsernames():
                print(f"- {username}")

        elif choice == "2":
            uname = input("Enter username to view profile: ").strip()
            person = graph.getProfile(uname)
            if person:
                print(person)
            else:
                print("User not found.")

        elif choice == "3":
            uname = input("Enter username to view who they follow: ").strip()
            following = graph.getFollowing(uname)
            if following:
                for u in following:
                    print(f"- {u}")
            else:
                print("No following found or user not found.")

        elif choice == "4":
            uname = input("Enter username to view their followers: ").strip()
            followers = graph.getFollowers(uname)
            if followers:
                for u in followers:
                    print(f"- {u}")
            else:
                print("No followers found or user not found.")

        elif choice == "5":
            break

        elif choice == "6":
            follower = input("Enter your username: ").strip()
            followee = input("Enter the username you want to follow: ").strip()
            if follower == followee:
                print("You cannot follow yourself.")
            elif follower in graph.getAllUsernames() and followee in graph.getAllUsernames():
                graph.follow(follower, followee)
            else:
                print("Invalid username(s).")

        elif choice == "7":
            follower = input("Enter your username: ").strip()
            followee = input("Enter the username you want to unfollow: ").strip()
            if follower == followee:
                print("You cannot unfollow yourself.")
            elif follower in graph.getAllUsernames() and followee in graph.getAllUsernames():
                graph.unfollow(follower, followee)
            else:
                print("Invalid username(s).")

        elif choice == "8":
            username = input("Enter new username: ").strip()
            name = input("Enter full name: ").strip()
            gender = input("Enter gender: ").strip()
            bio = input("Enter biography (optional): ").strip()
            privacy_input = input("Make profile private? (yes/no): ").strip().lower()
            is_private = privacy_input == "yes"

            new_user = Person(username, name, gender, bio, is_private)
            graph.addUser(new_user)

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    graph = setupSampleGraph()
    menu(graph)
