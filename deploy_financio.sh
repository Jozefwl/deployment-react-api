# define the repository and directories
REPO_URL="https://github.com/Miki-Herman/Financio"
PROJECT_DIR="Financio"
CLIENT_DIR="financio-client"

# clone or pull the latest project
if [ -d "$PROJECT_DIR" ]; then
    # if directory exists pull from git
    echo "Pulling latest changes for $PROJECT_DIR"
    cd "$PROJECT_DIR"
    git pull origin main
    cd ..
else
    # if directory does not exist clone from git
    echo "Cloning repository $REPO_URL"
    git clone "$REPO_URL"
fi

# change to client directory
cd "$PROJECT_DIR/$CLIENT_DIR"

# install dependencies and build the project
echo "Building the project"
npm install
npm run build

# remove the contents of /var/www
echo "Clearing /var/www"
sudo rm -rf /var/www/*

# copy the new build to /var/www
echo "Copying new build to /var/www"
sudo cp -R build/* /var/www/

# restart nginx.service
echo "Restarting NGINX service"
systemctl restart nginx

echo "Deployment complete"
