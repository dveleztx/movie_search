# Program    : Movie Search App
# Author     : David Velez
# Date       : 07/18/18
# Description: Movie Searching App running against movie_service.talkpython.fm
#              that returns a list of movies based upon user search input

# Imports
import movie_svc
import requests.exceptions


# Main Function
def main():
    print_header()
    search_event_loop()


# Print the Header
def print_header():
    print("------------------------")
    print("    Movie Search App")
    print("------------------------")
    print()


# Search Logic
def search_event_loop():
    search = "ONCE_THROUGH_LOOP"

    while search != "x":
        try:
            search = input("Movie search text (x to exit): ")
            if search != "x":
                results = movie_svc.find_movies(search)
                print("Found {} results.".format(len(results)))
                for r in results:
                    print("{} -- {}".format(
                        r.year, r.title
                    ))
                print()
        except ValueError:
            print("Error: Search text is required")
        except Exception as requests.exceptions.ConnectionError as ce:
            print("Error: Your network is down.")
        except Exception as x:
            print("Unexpected error. Details: {}".format(x))

    print("exiting...")


# Main
if __name__ == "__main__":
    main()
