# Copyright 2018 BMW Car IT GmbH
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.


from zuul.ansible import paths
command = paths._import_ansible_action_plugin("command")


class ActionModule(command.ActionModule):

    def run(self, tmp=None, task_vars=None):
        # we need the zuul_log_id on shell and command tasks
        if self._task.action in (
                'command', 'shell',
                'ansible.builtin.command', 'ansible.builtin.shell'):
            # This is a bit lame, but we do not log loops in the
            # zuul_stream.py callback.  This allows us to not write
            # out command.py output to files that will never be read.
            if 'ansible_loop_var' in task_vars:
                self._task.args['zuul_log_id'] = 'in-loop-ignore'
            else:
                # Get a unique key for ZUUL_LOG_ID_MAP.  ZUUL_LOG_ID_MAP
                # is read-only since we are forked.  Use it to add a
                # counter to the log id so that if we run the same task
                # more than once, we get a unique log file.  See comments
                # in paths.py for details.
                log_host = paths._sanitize_filename(
                    task_vars.get('inventory_hostname'))
                key = "%s-%s" % (self._task._uuid, log_host)
                count = paths.ZUUL_LOG_ID_MAP.get(key, 0)
                self._task.args['zuul_log_id'] = "%s-%s-%s" % (
                    self._task._uuid, count, log_host)
        return super(ActionModule, self).run(tmp, task_vars)
