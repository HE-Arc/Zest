# config valid for current version and patch releases of Capistrano
lock "~> 3.16.0"

set :application, "Zest"
set :projectname, "zestproject"
set :repo_url, "https://github.com/HE-Arc/Zest.git"

set :branch, "develop"

namespace :uwsgi do
    desc 'Restart application'
    task :restart do
        on roles(:web) do |h|
	        execute :sudo, 'sv reload uwsgi'
	    end
    end
end

namespace :python do
    def venv_path
        File.join(shared_path, 'env')
    end

    desc 'Create venv'
    task :create_venv do
        on roles([:app, :web]) do |h|
	    execute "sudo -u www-data python3 -m venv #{venv_path}"
            	execute "source #{venv_path}/bin/activate"
	    execute "#{venv_path}/bin/pip install -r #{release_path}/back/requirements"
        end
    end

    desc 'Config file environement'
    task :django_config do
        on roles([:app, :web]) do |h|
            def config_path
                File.join(shared_path, 'config/env.py')
            end

            def upload_src_path
                File.join(shared_path, "uploads")
            end

            def upload_target_path
                File.join(release_path, "back/#{fetch(:projectname)}/uploads")
            end

            def target_path
                File.join(release_path, "back/#{fetch(:projectname)}/#{fetch(:projectname)}/env.py")
            end

            info "config file #{config_path}"
            if test("[ -f #{config_path} ]")
                info "Env config file found"
                
                if test("[ -f #{target_path} ]")
                    info "Remove old sym link"
                    execute "rm #{target_path}"
                end
                info "Creating symlink"
                execute "ln -s #{config_path} #{target_path}"
            end
            
            info "Setup upload symlink"
            execute "ln -s #{upload_src_path} #{upload_target_path}"

        end
    end


    desc 'Django Migrations'
    task :django_migration do
        on roles([:app, :web]) do |h|
	    execute "#{venv_path}/bin/python #{release_path}/back/zestproject/manage.py migrate"
        end
    end
end

namespace :npm do
    def front_path
        File.join(release_path, 'front')
    end

    desc 'NPM install dependencies'
    task :install do
        on roles(:web) do |h|
            execute "cd '#{front_path}'; npm install"
        end
    end

    desc 'VueJs build app'
    task :build do
        on roles(:web) do |h|
            execute "cd '#{front_path}'; npm run build"
        end
    end
end

after 'deploy:publishing', 'uwsgi:restart'
after 'deploy:updating', 'python:create_venv'
after 'python:create_venv', 'python:django_config'
after 'python:django_config', 'python:django_migration'
after 'python:django_migration', 'npm:install'
after 'npm:install', 'npm:build'

# Default branch is :master
# ask :branch, `git rev-parse --abbrev-ref HEAD`.chomp

# Default deploy_to directory is /var/www/my_app_name
# set :deploy_to, "/var/www/my_app_name"

# Default value for :format is :airbrussh.
# set :format, :airbrussh

# You can configure the Airbrussh format using :format_options.
# These are the defaults.
# set :format_options, command_output: true, log_file: "log/capistrano.log", color: :auto, truncate: :auto

# Default value for :pty is false
# set :pty, true

# Default value for :linked_files is []
# append :linked_files, "config/database.yml"

# Default value for linked_dirs is []
# append :linked_dirs, "log", "tmp/pids", "tmp/cache", "tmp/sockets", "public/system"

# Default value for default_env is {}
# set :default_env, { path: "/opt/ruby/bin:$PATH" }

# Default value for local_user is ENV['USER']
# set :local_user, -> { `git config user.name`.chomp }

# Default value for keep_releases is 5
# set :keep_releases, 5

# Uncomment the following to require manually verifying the host key before first deploy.
# set :ssh_options, verify_host_key: :secure
