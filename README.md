Jumbleberry Server Credentials
=================================

#### Requirements:
Install and configure the [Jumbleberry Development Environment](https://github.com/Jumbleberry/Chef).

#### Usage:

##### Shadowers
1. Execute the passgen script in from the terminal
  
```
python passgen.py
```  

2. Follow along the prompts by choosing a unique password. This will be used for the sole purpose of granting `sudo` access on Jumbleberry infrastructure.
3. Append the generated hash to the end of the `shadowers` file, and commit it.

##### SSH
1. Generate a new SSH key. Make sure the key you generate has a secure passphrase.  
  
```
ssh-keygen -t rsa -C "your_email@jumbleberry"
```
2. Locate the public key for the generated SSH key. Usually found in `~/.ssh/`.
3. Locate the `comment` field on the generated SSH key (the very last string found in the public key file), and replace it with a string of the form DDMMYYYY_your_email@jumbleberry.com  
Ex. 

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC4M/lig+shrC0viHtdlx3I2tQsDNuOOwMIrSmLz3H6KXH0SRB5DUbaBTwT1A6NZ1bYEGNyfFXvgVn6qc+aBZ0qTQ5gA+9KUnWSc0ExEzCapZUrBRBOEbJpEKk8X+Zr1F1iTfBqgA6qLHYgHigUp7pqhWJqonMOgfSY/W7JLdXG1hSiqOhsvB2qlLGQsokniCS67DhrkS3dCWFHFrymsP52S5VKXFefNA3JESRbIYgzuhBGCwRIzEa4AW8kWIdCSwNFUK2QEOvSj4ElkjNKJzBZtWEr2K3wj72nDd58R2czanBhtCis1MiBPCDi2o3E9e+T2pRKIo3KUaKyI0iOEb5X IANE@JB-IANE01.local
```
would be modified to:

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC4M/lig+shrC0viHtdlx3I2tQsDNuOOwMIrSmLz3H6KXH0SRB5DUbaBTwT1A6NZ1bYEGNyfFXvgVn6qc+aBZ0qTQ5gA+9KUnWSc0ExEzCapZUrBRBOEbJpEKk8X+Zr1F1iTfBqgA6qLHYgHigUp7pqhWJqonMOgfSY/W7JLdXG1hSiqOhsvB2qlLGQsokniCS67DhrkS3dCWFHFrymsP52S5VKXFefNA3JESRbIYgzuhBGCwRIzEa4AW8kWIdCSwNFUK2QEOvSj4ElkjNKJzBZtWEr2K3wj72nDd58R2czanBhtCis1MiBPCDi2o3E9e+T2pRKIo3KUaKyI0iOEb5X 08062016_ian@jumbleberry.com
```  

Specifically, `IANE@JB-IANE01.local` becomes `08062016_ian@jumbleberry.com`.

4. Append the generated SSH key with modified comment field to the `ssh` file, and commit it.