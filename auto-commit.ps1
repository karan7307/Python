# Auto-commit and push script for Git
$repoPath = "d:\Python Program"
$lastCommitTime = Get-Date

while ($true) {
    cd $repoPath
    
    # Check for changes
    $status = git status --porcelain
    
    if ($status) {
        Write-Host "Changes detected at $(Get-Date)" -ForegroundColor Green
        
        # Stage all changes
        git add .
        
        # Commit with timestamp
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        git commit -m "Auto-commit: $timestamp"
        
        # Push to GitHub (both master and main)
        git push origin master
        git push origin main
        git push --all
        
        Write-Host "Committed and pushed successfully" -ForegroundColor Green
    }
    else {
        Write-Host "No changes detected at $(Get-Date)" -ForegroundColor Yellow
    }
    
    # Wait 5 minutes before checking again
    Start-Sleep -Seconds 300
}
