# Add a new user to Active Directory
Import-Module ActiveDirectory

$Username = "j.doe"
$Password = ConvertTo-SecureString "Password123!" -AsPlainText -Force
New-ADUser -Name "John Doe" -SamAccountName $Username -AccountPassword $Password -Enabled $true -Path "OU=Staff,DC=company,DC=com"

Write-Host "AD User created successfully: $Username"
