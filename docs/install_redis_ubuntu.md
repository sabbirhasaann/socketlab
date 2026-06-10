# Install Redis in Ubuntu

Installing Redis on Ubuntu is quick and easy using the default APT package manager. In just a few commands, you will have the Redis server downloaded, enabled, and ready to use for caching or as a message broker.

Here is the step-by-step guide to get you set up:

Step 1: Update the package listsFirst, open your terminal and update your local Ubuntu package index to ensure you get the latest version available:

```bash
sudo apt update
```

Step 2: Install the Redis serverInstall the official Redis package by running the following command:

```bash
sudo apt install redis-server -y
```

Step 3: Enable Redis to start on bootBy default, the Redis service should start automatically, but it is good practice to ensure it is explicitly enabled to boot up whenever your server restarts:

```bash
sudo systemctl enable redis-server
```

Step 4: Verify the Redis statusConfirm that Redis is successfully installed and currently running on your system:

```bash
sudo systemctl status redis-server
```
Look for the active (running) status in the output.

Step 5: Test the Redis connectionYou can easily test if your Redis server is functioning by connecting to it with the Redis command-line interface:

```bash
redis-cli
```

Once you are in the redis-cli shell, type ping:textping

If everything is working perfectly, Redis will respond with PONG. To exit the CLI, simply type exit.

Step 6 (Optional): Configure for production

If you plan on using Redis for a production application, you will want to fine-tune a couple of settings in the configuration file.

1. Edit the configuration file: Open it using your preferred terminal text editor:

```bash
sudo nano /etc/redis/redis.conf
```

2. Update the supervised directive: 

Since Ubuntu uses systemd, locate the line supervised no and change it to supervised systemd:

```text
supervised systemd
```

3. Save and exit: Press CTRL + O, then Enter to save, and CTRL + X to exit the nano editor.

4. Restart the service: Apply your changes by restarting the Redis server:

```bash
sudo systemctl restart redis-server
```

Resource
https://www.youtube.com/watch?v=E3Nm45Qwnog
