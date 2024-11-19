from tableActions.peopleActions import fillPeople
from tableActions.allStarFullActions import fillAllStartFull
from tableActions.appearancesActions import fillAppearances
from tableActions.awardsActions import fillAwards
from tableActions.awardsShareActions import fillAwardsShare
from tableActions.battingActions import fillBatting
from tableActions.battingPostActions import fillBattingPost
from tableActions.collegePlayingActions import fillCollegePlaying
from tableActions.fieldingPostActions import fillFieldingPost
from tableActions.hallOfFameActions import fillHallOfFame
from tableActions.homeGamesActions import fillHomeGame
from tableActions.managersActions import fillManagers
from tableActions.pitchingActions import fillPitching
from tableActions.pitchingPostActions import fillPostPitching
from tableActions.seriesPostActions import fillSeriesPost
from tableActions.teamActions import fillTeams

def updateDB():
    try:
        fillPeople()
        fillAllStartFull()
        fillAppearances()
        fillAwards()
        fillAwardsShare()
        fillBatting()
        fillBattingPost()
        fillCollegePlaying()
        fillFieldingPost()
        fillHallOfFame()
        fillHomeGame()
        fillManagers()
        fillPitching()
        fillPostPitching()
        fillSeriesPost()
        fillTeams()
    except Exception as e:
        print(e)
    finally:
        print('Database updated')

if __name__ == "__main__":
    updateDB()