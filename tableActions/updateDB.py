from tableActions import fillFielding
from tableActions.create_draft_table import create_draft_table
from tableActions.negroLeagueActions import update_negro_league_table
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
from tableActions.DraftActions import fillDraft
from tableActions.create_users_table import create_users_table
from tableActions.addGuestUser import create_guest_user
from tableActions.create_banned_users_table import create_banned_users_table
from tableActions.alterParks import create_parks_columns, update_lat_longitude
from tableActions.addAdmin import create_admin_user
from tableActions.create_user_logs_table import create_user_logs_table
from tableActions.alterParks import update_lat_longitude


def updateDB():
    try:
        steps = [
            fillPeople,fillPitching, fillFielding, fillAllStartFull,
            fillAppearances,fillAwards, fillAwardsShare, fillBatting, fillBattingPost,
            fillCollegePlaying, update_lat_longitude, fillFieldingPost,
            fillHallOfFame, fillHomeGame, fillManagers,
            fillPostPitching, fillSeriesPost, create_draft_table,
            fillDraft, fillTeams, create_users_table, create_guest_user,
            create_banned_users_table, create_user_logs_table, update_negro_league_table, create_admin_user,
        ]
        for step in steps:
            print(f"Running: {step.__name__}")
            step()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print('Database updated')

if __name__ == "__main__":
    updateDB()