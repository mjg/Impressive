##### GLOBAL VARIABLES #########################################################

# initialize private variables
DocumentTitle = None
FileName = ""
FileList = []
InfoScriptPath = None
AvailableRenderers = []
PDFRenderer = None
BaseWorkingDir = '.'
Marking = False
Tracing = False
Panning = False
FileProps = {}
PageProps = {}
PageCache = {}
CacheFile = None
CacheFileName = None
CacheFilePos = 0
CacheMagic = ""
MPlayerProcess = None
VideoPlaying = False
MarkValid, MarkBaseX, MarkBaseY = False, 0, 0
PanValid, PanBaseX, PanBaseY = False, 0, 0
MarkUL = (0, 0)
MarkLR = (0, 0)
ZoomX0 = 0.0
ZoomY0 = 0.0
ZoomArea = 1.0
ZoomMode = False
BoxZoom = False  # note: when active, contains the box coordinates
IsZoomed = 0
ViewZoomFactor = 1
ResZoomFactor = 1
HighResZoomFailed = False
TransitionRunning = False
TransitionDone = False
TransitionPhase = 0.0
CurrentCaption = 0
OverviewNeedUpdate = False
FileStats = None
OSDFont = None
CurrentOSDCaption = ""
CurrentOSDPage = ""
CurrentOSDStatus = ""
CurrentOSDComment = ""
Lrender = create_lock()
Lcache = create_lock()
Loverview = create_lock()
RTrunning = False
RTrestart = False
StartTime = 0
CurrentTime = 0
PageEnterTime = 0
PageLeaveTime = 0
PageTimeout = 0
NextPageAfterVideo = False
TimeDisplay = False
FirstPage = True
ProgressBarPos = 0
CursorVisible = True
CursorOnScreen = True
OverviewMode = False
LastPage = 0
WantStatus = False
GLVendor = ""
GLRenderer = ""
GLVersion = ""
RequiredShaders = []
DefaultScreenTransform = (-1.0, 1.0, 2.0, -2.0)
ScreenTransform = DefaultScreenTransform
SpotVertices = None
SpotIndices = None
CallQueue = []

# tool constants (used in info scripts)
FirstTimeOnly = 2
