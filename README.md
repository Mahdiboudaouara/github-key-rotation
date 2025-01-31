# 🚀 *Automated GitHub SSH Key Rotation*

Automatically rotate your GitHub SSH key with rollback, scheduling, and notifications.

## ✨ *Features*
* **Automated Key Rotation** – Generates and updates your GitHub SSH key.  
* **GitHub API Integration** – Replaces the old key securely.  
* **Rollback Mechanism** – Restores the old key if needed.  
* **Cron Job Scheduling** – Runs automatically every few months.  
* **Email & Slack Notifications** – Alerts on success or failure.  

## 🔧 *How It Works*
1. Generates a new SSH key and updates GitHub.  
2. Updates local SSH configuration.  
3. Deletes the old key with a backup.  
4. Notifies via email or Slack.  
5. Runs automatically using cron.  

## 🚀 *Future Improvements*
* Multi-platform support (GitHub, GitLab, Bitbucket).  
* Encryption for private keys.  
* Interactive CLI for manual rotation.  

Stay secure with **automated SSH key management!** 🔒  
