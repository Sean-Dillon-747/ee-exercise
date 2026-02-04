# Create a folder under the drive root
mkdir actions-runner
cd actions-runner
# Download the latest runner package
#Invoke-WebRequest -Uri https://github.com/actions/runner/releases/download/v2.331.0/actions-runner-win-x64-2.331.0.zip -OutFile actions-runner-win-x64-2.331.0.zip
# Optional: Validate the hash
if((Get-FileHash -Path actions-runner-win-x64-2.331.0.zip -Algorithm SHA256).Hash.ToUpper() -ne '473e74b86cd826e073f1c1f2c004d3fb9e6c9665d0d51710a23e5084a601c78a'.ToUpper()){ throw 'Computed checksum did not match' }
# Extract the installer
Add-Type -AssemblyName System.IO.Compression.FileSystem ; [System.IO.Compression.ZipFile]::ExtractToDirectory("$PWD/actions-runner-win-x64-2.331.0.zip", "$PWD")

# Configure the runner
./config.cmd  --unattended --url https://github.com/Sean-Dillon-747/ee-exercise --token AQRULM3FFBKTHMDZG7CURSDJQNI3W
# Install the service
./run.cmd