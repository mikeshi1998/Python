# Yuchen Shi
# ITP115, Spring 2018
# Assignment 7
# yuchensh@usc.edu

import MusicLibraryHelper
import random

def displayMenu():
    print("Welcome to Your Music Library\nOptions:\n\t1) Display library\n\t2) Display all artists\n\t3) Add an album\n\t4) Delete an album\n\t5) Delete an artist\n\t6) Search library\n\t7) Generate a random playlist\n\t8) Exit")


def displayLibrary(musicLibDictionary):
    for key in musicLibDictionary:
        print("Artist:", key, "\nAlbums:")
        for album in musicLibDictionary[key]:
            print("\t-", album)

def displayArtists(musicLibDictionary):
    artistsList=musicLibDictionary.keys()
    print("Displaying all artists:")
    for artist in artistsList:
        print("-", artist)

def addAlbum(musicLibDictionary):
    addArtist=input("Enter an artist: ")
    addArtistTitle=addArtist.title()
    addAlbum=input("Enter an album: ")
    addAlbumTitle=addAlbum.title()
    artistsList = musicLibDictionary.keys()
    if addArtistTitle in artistsList:
        if addAlbumTitle not in musicLibDictionary[addArtistTitle]:
            musicLibDictionary[addArtistTitle].append(addAlbumTitle)
    else:
        musicLibDictionary[addArtistTitle]=[addAlbumTitle]

def deleteAlbum(musicLibDictionary):
    deleteArtist=input("Enter an artist: ")
    deleteArtistTitle=deleteArtist.title()
    deleteAlbum=input("Enter an album: ")
    deleteAlbumTitle=deleteAlbum.title()
    artistsList = musicLibDictionary.keys()
    if deleteArtistTitle in artistsList:
        if deleteAlbumTitle in musicLibDictionary[deleteArtistTitle]:
            musicLibDictionary[deleteArtistTitle].remove(deleteAlbumTitle)
            if len(musicLibDictionary[deleteArtistTitle])==0:
                del musicLibDictionary[deleteArtistTitle]
            return True
        else:
            return False
    else:
        return False

def deleteArtist(musicLibDictionary):
    deleteArtist = input("Enter an artist: ")
    deleteArtistTitle = deleteArtist.title()
    artistsList = musicLibDictionary.keys()
    if deleteArtistTitle in artistsList:
        del musicLibDictionary[deleteArtistTitle]
        return True
    else:
        return False

def searchLibrary(musicLibDictionary):
    searchTerm=input("Please enter a search term: ")
    artistsList = musicLibDictionary.keys()
    albumsList=musicLibDictionary.values()
    searchTermTitle=searchTerm.title()
    artistResultList=[]
    albumResultList=[]
    for artist in artistsList:
        if artist == searchTermTitle:
            if artist not in artistResultList:
                artistResultList.append(artist)
        delimiter=" "
        artistWordList=artist.split(delimiter)
        for word in artistWordList:
            wordTitle=word.title()
            if wordTitle == searchTermTitle:
                if artist not in artistResultList:
                    artistResultList.append(artist)
        artistCharacterList=list(artist)
        for character in artistCharacterList:
            if character.lower() == searchTermTitle.lower():
                if artist not in artistResultList:
                    artistResultList.append(artist)
    for albums in albumsList:
        for album in albums:
            if album == searchTermTitle:
                if album not in albumResultList:
                    albumResultList.append(album)
            delimiter=" "
            albumWordList=album.split(delimiter)
            for word in albumWordList:
                wordTitle=word.title()
                if wordTitle==searchTermTitle:
                    if album not in albumResultList:
                        albumResultList.append(album)
            albumCharacterList=list(album)
            for character in albumCharacterList:
                if character.lower() == searchTermTitle.lower():
                    if album not in albumResultList:
                        albumResultList.append(album)
    print("Artists containing '" + searchTerm + "'")
    if len(artistResultList)==0:
        print("\tNo results")
    else:
        for artist in artistResultList:
            print("-", artist)
    print("Albums containing '" + searchTerm + "'")
    if len(albumResultList)==0:
        print("\tNo results")
    else:
        for album in albumResultList:
            print("-", album)

def generateRandomPlaylist(musicLibDictionary):
    print("Here is your random playlist:")
    for key in musicLibDictionary:
        index=random.randrange(0, len(musicLibDictionary[key]))
        print("-", musicLibDictionary[key][index], "by", key)

def main():
    choice=1
    musicLibDictionary = MusicLibraryHelper.loadLibrary("musicLibrary.dat")
    while choice != 8:
        displayMenu()
        choice=int(input("> "))
        while choice not in [1, 2, 3, 4, 5, 6, 7, 8]:
            choice=int(input("Invalid choice. Please try again. "))
        if choice == 1:
            displayLibrary(musicLibDictionary)
        elif choice == 2:
            displayArtists(musicLibDictionary)
        elif choice == 3:
            addAlbum(musicLibDictionary)
        elif choice == 4:
            deleteOrNot=deleteAlbum(musicLibDictionary)
            if deleteOrNot is True:
                print("Delete album success!")
            else:
                print("Delete album failed.")
        elif choice == 5:
            deleteOrNot2=deleteArtist(musicLibDictionary)
            if deleteOrNot2 is True:
                print("Delete artist success!")
            else:
                print("Delete artist failed.")
        elif choice == 6:
            searchLibrary(musicLibDictionary)
        elif choice == 7:
            generateRandomPlaylist(musicLibDictionary)
    print("Saving music library...")
    MusicLibraryHelper.saveLibrary("musicLibrary.dat", musicLibDictionary)
    print("Goodbye!")

main()
