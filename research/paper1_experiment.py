

        #   Both client & server
        stdin, stdout, stderr = client.exec_command('sudo apt-get update')
        stdin, stdout, stderr = client.exec_command('sudo apt-get install wine')
        stdin, stdout, stderr = client.exec_command('wget https://dord.mynetgear.com/rapidlasso.zip')
        stdin, stdout, stderr = client.exec_command('unzip rapidlasso.zip')
        stdin, stdout, stderr = client.exec_command('lasground')
        stdin, stdout, stderr = client.exec_command('lasmerge')