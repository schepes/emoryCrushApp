import aws_cdk as cdk
from backend.backend_stack import CrushEmoryBackendStack

app = cdk.App()
CrushEmoryBackendStack(app, "CrushEmoryBackendStack")
app.synth()
