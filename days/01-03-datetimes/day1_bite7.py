from datetime import datetime

loglines = ["ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file, resetting to empty.",
"ERROR 2014-07-03T23:24:31 supybot Exact error: IOError: [Errno 2] No such file or directory: 'conf/users.conf'",
"ERROR 2014-07-03T23:24:31 supybot Invalid channel database, resetting to empty.",
"ERROR 2014-07-03T23:24:31 supybot Exact error: IOError: [Errno 2] No such file or directory: 'conf/channels.conf'",
"WARNING 2014-07-03T23:24:31 supybot Couldn't open ignore database: [Errno 2] No such file or directory: 'conf/ignores.conf'",
"INFO 2014-07-03T23:27:51 supybot Shutdown initiated.",
"INFO 2014-07-03T23:27:51 supybot Killing Driver objects.",
"INFO 2014-07-03T23:27:51 supybot Killing Irc objects.",
"INFO 2014-07-03T23:27:51 supybot Shutdown complete.",
"INFO 2014-07-03T23:30:37 supybot Creating new Irc for freenode.",
"INFO 2014-07-03T23:30:37 supybot Connecting to irc.freenode.net:8001.",
"INFO 2014-07-03T23:30:38 supybot Loading plugins (connecting to freenode).",
"INFO 2014-07-03T23:30:46 supybot Server orwell.freenode.net has version ircd-seven-1.1.3",
"INFO 2014-07-03T23:30:48 supybot Got end of MOTD from orwell.freenode.net",
"INFO 2014-07-03T23:30:54 supybot Join to #timvideos on freenode synced in 2.41 seconds.",
"INFO 2014-07-03T23:31:22 supybot Exiting due to Ctrl-C.  If the bot doesn't exit within a few seconds, feel free to press Ctrl-C again to make it exit without flushing its message queues.",
"INFO 2014-07-03T23:31:22 supybot Flushers flushed and garbage collected.",
"INFO 2014-07-03T23:31:22 supybot Driver for Irc object for freenode dying.",
"INFO 2014-07-03T23:31:22 supybot Irc object for freenode dying.",
"INFO 2014-07-03T23:31:22 supybot Driver for Irc object for freenode dying.",
"WARNING 2014-07-03T23:31:22 supybot Disconnect from irc.freenode.net:8001: error: [Errno 9] Bad file descriptor.",
"INFO 2014-07-03T23:31:22 supybot Reconnecting to freenode at 2014-07-03T23:31:32.",
"INFO 2014-07-03T23:31:22 supybot Removing driver SocketDriver(Irc object for freenode).",
"INFO 2014-07-03T23:31:22 supybot Total uptime: 45 seconds.",
"INFO 2014-07-03T23:31:22 supybot Total CPU time taken: 1.12 seconds.",
"INFO 2014-07-03T23:31:22 supybot No more Irc objects, exiting.",
"INFO 2014-07-03T23:31:22 supybot Shutdown initiated.",
"INFO 2014-07-03T23:31:22 supybot Killing Driver objects.",
"INFO 2014-07-03T23:31:22 supybot Killing Irc objects.",
"INFO 2014-07-03T23:31:22 supybot Writing registry file to planet-news.conf",
"INFO 2014-07-03T23:31:22 supybot Finished writing registry file.",
"INFO 2014-07-03T23:31:22 supybot Shutdown complete."]


def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    return datetime.strptime(line.split(" ")[1], "%Y-%m-%dT%H:%M:%S")


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    initiate = []
    for line in loglines:
        line_split = line.rstrip().split(" ")
        if " ".join(line_split[-2:]) == "Shutdown initiated.":
            initiate.append(convert_to_datetime(line))
    print(initiate)
    return initiate[-1] - initiate[0]

line1 = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file'
line2 = 'INFO 2015-10-03T10:12:51 supybot Shutdown initiated.'
line3 = 'INFO 2016-09-03T02:11:22 supybot Shutdown complete.'

a = convert_to_datetime(line1)
b = convert_to_datetime(line2)

print(time_between_shutdowns(loglines))
