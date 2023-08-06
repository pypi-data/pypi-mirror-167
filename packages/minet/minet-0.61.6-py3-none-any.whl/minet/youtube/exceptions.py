# =============================================================================
# Minet YouTube Exceptions
# =============================================================================
#
from minet.exceptions import MinetError


class YouTubeError(MinetError):
    pass


class YouTubeInvalidAPIKeyError(YouTubeError):
    pass


class YouTubeInvalidAPICall(YouTubeError):
    def __init__(self, url, status, data):
        super().__init__()
        self.url = url
        self.status = status
        self.data = data

    def __str__(self):
        return super().__str__() + ", Url: %s, Status: %i, Data: %s" % (
            self.url,
            self.status,
            self.data,
        )


class YouTubeInvalidVideoTarget(YouTubeError):
    pass


class YouTubeInvalidChannelTarget(YouTubeError):
    pass


class YouTubeDisabledComments(YouTubeError):
    pass


class YouTubeVideoNotFound(YouTubeError):
    pass
