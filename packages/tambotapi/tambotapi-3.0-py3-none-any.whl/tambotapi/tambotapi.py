import json
import logging
import os
import time

import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class TamBot:
    def __init__(self, token):
        self.token = token
        self.url = 'https://botapi.tamtam.chat/'
        self.marker = None

    def get_updates(self, limit=1, timeout=45):
        update = {}
        method = 'updates'
        params = {
            "marker": self.marker,
            "limit": limit,
            "timeout": timeout,
            "types": None,
            "access_token": self.token
        }
        try:
            response = requests.get(self.url + method, params, timeout=60)
            update = response.json()
        except requests.exceptions.ReadTimeout:
            logger.info('get_updates ReadTimeout')
        except requests.exceptions.ConnectionError:
            logger.error('get_updates ConnectionError')
            time.sleep(1)
        except requests.exceptions.RequestException as e:
            logger.error('get_updates Request Error: {}'.format(e))
        except Exception as e:
            logger.error(('get_updates General Error: {}'.format(e)))
        if 'updates' in update.keys():
            if len(update['updates']) != 0:
                self.mark_seen(chat_id=self.get_chat_id(update))
            else:
                update = None
        else:
            update = None
        if update:
            self.marker = self.get_marker(update)
        return update

    def get_subscriptions(self):
        method = 'subscriptions'
        params = {
            "access_token": self.token,
        }
        try:
            response = requests.get(self.url + method, params=params)
            if response.status_code == 200:
                subscriptions = response.json()
            else:
                logger.error("Error get subscriptions: {}".format(response.status_code))
                subscriptions = None
        except Exception as e:
            logger.error("Error connect get subscriptions: %s.", e)
            subscriptions = None
        return subscriptions

    def subscribe(self, url, update_types, version):
        method = 'subscriptions'
        params = {
            "access_token": self.token,
        }
        data = {
            "url": url,
            "update_types": update_types,
            "version": version
        }
        try:
            response = requests.post(self.url + method, params=params, data=json.dumps(data))
            if response.status_code == 200:
                subscribe = response.json()
            else:
                logger.error("Error subscribes: {}".format(response.status_code))
                subscribe = None
        except Exception as e:
            logger.error("Error connect subscribes: %s.", e)
            subscribe = None
        return subscribe

    def unsubscribe(self, url):
        method = 'subscriptions'
        params = (
            ('access_token', self.token),
            ('url', url),
        )
        try:
            response = requests.delete(self.url + method, params=params)
            if response.status_code == 200:
                unsubscribe = response.json()
            else:
                logger.error("Error unsubscribe: {}".format(response.status_code))
                unsubscribe = None
        except Exception as e:
            logger.error("Error connect unsubscribe: %s.", e)
            unsubscribe = None
        return unsubscribe

    def get_marker(self, update):
        marker = None
        if update:
            marker = update['marker']
        return marker

    def get_bot_info(self):
        method = 'me'
        params = {
            "access_token": self.token,
        }
        try:
            response = requests.get(self.url + method, params=params)
            if response.status_code == 200:
                bot_info = response.json()
            else:
                logger.error("Error get bot info: {}".format(response.status_code))
                bot_info = None
        except Exception as e:
            logger.error("Error connect get bot info: %s.", e)
            bot_info = None
        return bot_info

    def get_bot_user_id(self):
        bot = self.get_bot_info()
        bot_user_id = bot['user_id']
        return bot_user_id

    def get_bot_name(self):
        bot = self.get_bot_info()
        name = bot['name']
        return name

    def get_bot_username(self):
        bot = self.get_bot_info()
        username = bot['username']
        return username

    def get_bot_avatar_url(self):
        bot = self.get_bot_info()
        if 'avatar_url' in bot:
            avatar_url = bot['avatar_url']
            return avatar_url

    def get_bot_full_avatar_url(self):
        bot = self.get_bot_info()
        if 'full_avatar_url' in bot:
            full_avatar_url = bot['full_avatar_url']
            return full_avatar_url

    def get_bot_commands(self):
        bot = self.get_bot_info()
        if 'commands' in bot:
            commands = bot['commands']
            return commands

    def get_bot_description(self):
        bot = self.get_bot_info()
        if 'description' in bot:
            description = bot['description']
            return description

    def command(self, name, description):
        com = {"name": "/{}".format(name), "description": description}
        return com

    def edit_bot_info(self, name, username=None, description=None, commands=None, photo=None, photo_url=None):
        method = 'me'
        params = {"access_token": self.token}
        photo_res = None
        if photo:
            photo = self.token_upload_content('image', photo)
            photo_res = {"url": photo}
        elif photo_url:
            photo_res = {"url": photo_url}
        data = {
            "name": name,
            "username": username,
            "description": description,
            "commands": commands,
            "photo": photo_res
        }
        try:
            response = requests.patch(self.url + method, params=params, data=json.dumps(data))
            if response.status_code == 200:
                edit_bot_info = response.json()
            else:
                logger.error("Error edit bot info: {}".format(response.status_code))
                edit_bot_info = None
        except Exception as e:
            logger.error("Error connect edit bot info: %s.", e)
            edit_bot_info = None
        return edit_bot_info

    def get_chat(self, chat_id):
        method = 'chats/{}'.format(chat_id)
        params = {
            "access_token": self.token
        }
        try:
            response = requests.get(self.url + method, params)
            if response.status_code == 200:
                chat = response.json()
            else:
                logger.error("Error get chat info: {}".format(response.status_code))
                chat = None
        except Exception as e:
            logger.error("Error connect get chat info: %s.", e)
            chat = None
        return chat

    def get_chat_type(self, update):
        chat_type = None
        if update is not None:
            if 'updates' in update.keys():
                upd = update['updates'][0]
            else:
                upd = update
            update_type = self.get_update_type(update)
            if update_type == 'message_created':
                upd1 = upd.get('message').get('recipient')
                if 'chat_type' in upd1.keys():
                    chat_type = upd1['chat_type']
                else:
                    chat_type = None
        return chat_type

    def get_all_chats(self, count=50, marker=None):
        method = 'chats'
        params = {
            "access_token": self.token,
            "count": count,
            "marker": marker
        }
        try:
            response = requests.get(self.url + method, params=params)
            if response.status_code == 200:
                chats = response.json()
            else:
                logger.error("Error get all chats: {}".format(response.status_code))
                chats = None
        except Exception as e:
            logger.error("Error connect get all chats: %s.", e)
            chats = None
        return chats

    def get_chat_admins(self, chat_id):
        method = 'chats/{}'.format(chat_id) + '/members/admins'
        params = {
            "access_token": self.token
        }
        try:
            response = requests.get(self.url + method, params=params)
            if response.status_code == 200:
                chat_admins = response.json()
            else:
                logger.info("It's not a chat or the bot is not an administrator. Chat_id: {}".format(chat_id))
                chat_admins = None
        except Exception as e:
            logger.error("Error connect get_chat_admins: %s.", e)
            chat_admins = None
        return chat_admins

    def get_chat_membership(self, chat_id):
        method = 'chats/{}'.format(chat_id) + '/members/me'
        params = {
            "access_token": self.token
        }
        try:
            response = requests.get(self.url + method, params=params)
            if response.status_code == 200:
                chat_membership = response.json()
            else:
                logger.error("Error chat membership: {}".format(response.status_code))
                chat_membership = None
        except Exception as e:
            logger.error("Error connect chat membership: %s.", e)
            chat_membership = None
        return chat_membership

    def leave_chat(self, chat_id):
        method = 'chats/{}'.format(chat_id) + '/members/me'
        params = {
            "access_token": self.token
        }
        try:
            response = requests.delete(self.url + method, params=params)
            if response.status_code == 200:
                leave_chat = response.json()
            else:
                logger.error("Error leave chat: {}".format(response.status_code))
                leave_chat = None
        except Exception as e:
            logger.error("Error connect leave chat: %s.", e)
            leave_chat = None
        return leave_chat

    def edit_chat_info(self, chat_id, icon=None, icon_url=None, title=None, pin=None, notify=True):
        method = 'chats/{}'.format(chat_id)
        auth = {
            "access_token": self.token
        }
        icon_res = None
        if icon:
            icon = self.token_upload_content('image', icon)
            icon_res = {"url": icon}
        elif icon_url:
            icon_res = {"url": icon_url}
        data = {
            "icon": icon_res,
            "title": title,
            "pin": pin,
            "notify": notify
        }
        try:
            response = requests.patch(self.url + method, params=auth, data=json.dumps(data))
            if response.status_code == 200:
                chat_info = response.json()
            else:
                logger.error("Error edit chat info: {}".format(response.status_code))
                chat_info = None
        except Exception as e:
            logger.error("Error connect edit chat info: %s.", e)
            chat_info = None
        return chat_info

    def get_members(self, chat_id, user_ids, marker=None, count=20):
        method = 'chats/{}'.format(chat_id) + '/members'
        params = {
            "access_token": self.token,
            'user_ids': [
                user_ids
            ],
            'marker': marker,
            'count': count
        }
        try:
            response = requests.get(self.url + method, params=params)
            if response.status_code == 200:
                members = response.json()
            else:
                logger.error("Error get members: {}".format(response.status_code))
                members = None
        except Exception as e:
            logger.error("Error connect get members: %s.", e)
            members = None
        return members

    def add_members(self, chat_id, user_ids):
        method = 'chats/{}'.format(chat_id) + '/members'
        params = {
            "access_token": self.token
        }
        data = {
            "user_ids": [
                user_ids
            ]
        }
        try:
            response = requests.post(self.url + method, params=params, data=json.dumps(data))
            if response.status_code == 200:
                add_members = response.json()
            else:
                logger.error("Error add members: {}".format(response.status_code))
                add_members = None
        except Exception as e:
            logger.error("Error connect add members: %s.", e)
            add_members = None
        return add_members

    def remove_member(self, chat_id, user_id):
        method = 'chats/{}'.format(chat_id) + '/members'
        params = (
            ('access_token', self.token),
            ('user_id', user_id),
        )
        try:
            response = requests.delete(self.url + method, params=params)
            if response.status_code == 200:
                remove_member = response.json()
            else:
                logger.error("Error remove member: {}".format(response.status_code))
                remove_member = None
        except Exception as e:
            logger.error("Error connect remove member: %s.", e)
            remove_member = None
        return remove_member

    def ban_member(self, chat_id, user_id, block=True):
        method = 'chats/{}'.format(chat_id) + '/members'
        params = (
            ('access_token', self.token),
            ('user_id', user_id),
            ('block', block),
        )
        try:
            response = requests.delete(self.url + method, params=params)
            if response.status_code == 200:
                ban_member = response.json()
            else:
                logger.error("Error ban member: {}".format(response.status_code))
                ban_member = None
        except Exception as e:
            logger.error("Error connect ban member: %s.", e)
            ban_member = None
        return ban_member

    def get_update_type(self, update):
        upd_type = None
        if update:
            if 'updates' in update.keys():
                upd = update['updates'][0]
            else:
                upd = update
            upd_type = upd.get('update_type')
        return upd_type

    def get_text(self, update):
        text = None
        if update:
            type = self.get_update_type(update)
            logger.info(type)
            if 'updates' in update.keys():
                update = update['updates'][0]
            if type == 'message_edited' or type == 'message_callback' or type == 'message_created' or type == 'message_constructed':
                try:
                    text = update['message']['body']['text']
                    if not text:
                        text = update['message']['link']['message']['text']
                except Exception as e:
                    logger.debug('get_text body none: %s', e)
                    try:
                        text = update['message']['link']['message']['text']
                    except Exception as e:
                        logger.debug('get_text link none: %s', e)
                        text = None
            elif type == 'message_construction_request':
                try:
                    upd = update['input']
                    if 'messages' in upd.keys():
                        if len(upd['messages']) >> 0:
                            text = upd['messages'][0]['text']
                except Exception as e:
                    logger.debug('get_text in construct none: %s', e)
                    text = None
            elif type == 'message_chat_created':
                upd = update['chat']
                if 'pinned_message' in upd.keys():
                    try:
                        text = upd['pinned_message']['body']['text']
                    except Exception as e:
                        logger.debug('get_text pinned_message none: %s', e)
                        try:
                            text = upd['pinned_message']['link']['message']['text']
                        except Exception as e:
                            logger.debug('get_text pinned_messsage link none: %s', e)
                            text = None
        return text

    def get_attachments(self, update):
        attachments = None
        if update:
            type = self.get_update_type(update)
            if 'updates' in update.keys():
                update = update['updates'][0]
            if type == 'message_edited' or type == 'message_callback' or type == 'message_created' or type == 'message_constructed':
                try:
                    attachments = update['message']['body']['attachments']
                except Exception as e:
                    logger.debug('get_attachments body none: %s', e)
                    try:
                        attachments = update['message']['link']['message']['attachments']
                    except Exception as e:
                        logger.debug('get_attachments link None: %s', e)
                        attachments = None
            elif type == 'message_construction_request':
                try:
                    upd = update['input']
                    if 'messages' in upd.keys():
                        if len(upd['messages']) >> 0:
                            attachments = upd['messages'][0]['attachments']
                except Exception as e:
                    logger.debug('get_attachments in construct: %s', e)
                    attachments = None
        return attachments

    def get_url(self, update):
        url = None
        attach = self.get_attachments(update)
        if attach:
            attach = attach[0]
            if 'payload' in attach.keys():
                attach = attach.get('payload')
                if 'url' in attach.keys():
                    url = attach.get('url')
        return url

    def get_attach_type(self, update):
        att_type = None
        attach = self.get_attachments(update)
        if attach:
            try:
                att_type = attach[0]['type']
            except Exception as e:
                logger.error('get_attach_type: %s', e)
                att_type = None
        return att_type

    def get_chat_id(self, update=None):
        chat_id = None
        if update is None:
            method = 'chats'
            params = {
                "access_token": self.token
            }
            try:
                response = requests.get(self.url + method, params=params)
                if response.status_code == 200:
                    update = response.json()
                    if 'chats' in update.keys():
                        update = update['chats'][0]
                        chat_id = update.get('chat_id')
                else:
                    logger.error("Error get_chat_id: {}".format(response.status_code))
            except Exception as e:
                logger.error("Error connect get_chat_id: %s.", e)
                chat_id = None
        else:
            type = self.get_update_type(update)
            if 'updates' in update.keys():
                update = update['updates'][0]
            if type == 'message_edited' or type == 'message_callback' or type == 'message_created':
                try:
                    chat_id = update['message']['recipient']['chat_id']
                except Exception as e:
                    logger.info('get_chat_id (message_edited) sender is None: %s', e)
            elif type == 'message_chat_created':
                chat_id = update['chat']['chat_id']
            elif type == 'message_constructed' or type == 'message_construction_request':
                chat_id = None
            elif type:
                try:
                    chat_id = update['chat_id']
                except Exception as e:
                    logger.error('get_chat_id: %s', e)
                # if type == 'message_created' or type == 'message_construction_request' or type == 'bot_added' or type
                # == 'bot_removed' or type == 'user_added' or type == 'user_removed' or type == '':
        return chat_id

    def get_link_chat_id(self, update):
        chat_id = None
        if update is not None:
            if 'updates' in update.keys():
                upd = update['updates'][0]
            else:
                upd = update
            if 'message' in upd.keys():
                upd = upd['message']
                if 'link' in upd.keys():
                    upd = upd['link']
                    if 'chat_id' in upd.keys():
                        chat_id = upd['chat_id']
        return chat_id

    def get_user_id(self, update):
        user_id = None
        """if update:
            if 'updates' in update.keys():
                upd = update['updates'][0]
            else:
                upd = update
            if 'message_id' in upd.keys():
                user_id = None
            elif 'chat_id' in upd.keys():
                user_id = upd['user']['user_id']
            elif 'callback' in upd.keys():
                user_id = upd['callback']['user']['user_id']
            elif 'session_id' in upd.keys():
                user_id = upd['user']['user_id']
            else:
                upd = upd['message']
                if 'sender' in upd.keys():
                    user_id = upd['sender']['user_id']
                else:
                    user_id = upd['recipient']['user_id']
        """
        if update:
            type = self.get_update_type(update)
            if 'updates' in update.keys():
                update = update['updates'][0]
            if type == 'message_chat_created':
                user_id = None
            elif type == 'message_edited' or type == 'message_created' or type == 'message_constructed':
                try:
                    user_id = update['message']['sender']['user_id']
                except Exception as e:
                    logger.info('get_user_id (message_created...) sender is None: %s', e)
            elif type == 'message_chat_created':
                try:
                    user_id = update['chat']['dialog_with_user']['user_id']
                except Exception as e:
                    logger.info('get_user_id (message_chat_created) is None: %s', e)
                if not user_id:
                    try:
                        user_id = update['chat']['pinned_message']['sender']['user_id']
                    except Exception as e:
                        logger.info('get_user_id (message_chat_created - pinned) is None: %s', e)
            elif type == 'message_removed':
                user_id = update['user_id']
            elif type == 'message_callback':
                user_id = update['callback']['user']['user_id']
            elif type:
                try:
                    user_id = update['user']['user_id']
                except Exception as e:
                    logger.error('get_user_id: %s', e)
        return user_id

    def get_link_user_id(self, update):
        user_id = None
        if update:
            if 'updates' in update.keys():
                upd = update['updates'][0]
            else:
                upd = update
            if 'message' in upd.keys():
                upd = upd['message']
                if 'link' in upd.keys():
                    upd = upd['link']
                    if 'sender' in upd.keys():
                        user_id = upd['sender']['user_id']
        return user_id

    def get_name(self, update):
        name = None
        if update:
            if 'updates' in update.keys():
                upd = update['updates'][0]
            else:
                upd = update
            if 'user' in upd.keys():
                name = upd['user']['name']
            elif 'callback' in upd.keys():
                name = upd['callback']['user']['name']
            elif 'chat' in upd.keys():
                upd = upd['chat']
                if 'dialog_with_user' in upd.keys():
                    name = upd['dialog_with_user']['name']
            elif 'message' in upd.keys():
                upd = upd['message']
                if 'sender' in upd.keys():
                    name = upd['sender']['name']
        return name

    def get_is_bot(self, update):
        is_bot = None
        if update:
            if 'updates' in update.keys():
                upd = update['updates'][0]
            else:
                upd = update
            if 'user' in upd.keys():
                is_bot = upd['user']['is_bot']
            elif 'callback' in upd.keys():
                is_bot = upd['callback']['user']['is_bot']
            elif 'chat' in upd.keys():
                upd = upd['chat']
                if 'dialog_with_user' in upd.keys():
                    is_bot = upd['dialog_with_user']['is_bot']
            elif 'message' in upd.keys():
                upd = upd['message']
                if 'sender' in upd.keys():
                    is_bot = upd['sender']['is_bot']
        return is_bot

    def get_link_name(self, update):
        name = None
        if update:
            if 'updates' in update.keys():
                upd = update['updates'][0]
            else:
                upd = update
            if 'message' in upd.keys():
                upd = upd['message']
                if 'link' in upd.keys():
                    upd = upd['link']
                    if 'sender' in upd.keys():
                        name = upd['sender']['name']
        return name

    def get_username(self, update):
        username = None
        if update:
            if 'updates' in update.keys():
                upd = update['updates'][0]
            else:
                upd = update
            if 'user' in upd.keys():
                upd = upd['user']
                if 'username' in upd.keys():
                    username = upd['username']
            elif 'callback' in upd.keys():
                upd = upd['callback']['user']
                if 'username' in upd.keys():
                    username = upd['username']
            elif 'chat' in upd.keys():
                upd = upd['chat']
                if 'dialog_with_user' in upd.keys():
                    upd = upd['dialog_with_user']
                    if 'username' in upd.keys():
                        username = upd['username']
            elif 'message' in upd.keys():
                upd = upd['message']
                if 'sender' in upd.keys():
                    upd = upd['sender']
                    if 'username' in upd.keys():
                        username = upd['username']
        return username

    def get_link_username(self, update):
        username = None
        if update:
            if 'updates' in update.keys():
                upd = update['updates'][0]
            else:
                upd = update
            if 'message' in upd.keys():
                upd = upd['message']
                if 'link' in upd.keys():
                    upd = upd['link']
                    if 'sender' in upd.keys():
                        upd = upd['sender']
                        if 'username' in upd.keys():
                            username = upd['username']
        return username

    def get_payload(self, update):
        payload = None
        if update:
            if 'updates' in update.keys():
                upd = update['updates'][0]
            else:
                upd = update
            type = self.get_update_type(update)
            if type == 'message_callback':
                upd = upd.get('callback')
                if 'payload' in upd.keys():
                    payload = upd.get('payload')
            elif type == 'message_construction_request':
                upd = upd.get('input')
                if upd.get('input_type') == 'callback':
                    payload = upd.get('payload')
        return payload

    def get_callback_id(self, update):
        callback_id = None
        type = self.get_update_type(update)
        if update:
            if 'updates' in update.keys():
                upd = update['updates'][0]
            else:
                upd = update
            if type == 'message_callback':
                upd = upd.get('callback')
                if 'callback_id' in upd.keys():
                    callback_id = upd.get('callback_id')
        return callback_id

    def get_session_id(self, update):
        session_id = None
        if update is not None:
            if 'updates' in update.keys():
                upd = update['updates'][0]
            else:
                upd = update
            if 'session_id' in upd.keys():
                session_id = upd.get('session_id')
        return session_id

    def get_message_id(self, update):
        mid = None
        if update:
            if 'updates' in update.keys():
                upd = update['updates'][0]
            else:
                upd = update
            type = self.get_update_type(update)
            #if type == 'message_created' or type == 'message_callback' or type == 'message_edited' or type == 'message_constructed':
            if 'message' in upd.keys():
                try:
                    mid = upd.get('message').get('body').get('mid')
                except Exception as e:
                    logger.info('get_message_id: {}'.format(e))
            elif 'message_id' in upd.keys():  # type == 'message_chat_created' or type == 'message_removed':
                mid = upd['message_id']
        return mid

    def get_start_payload(self, update):
        st_payload = None
        if update:
            if 'updates' in update.keys():
                upd = update['updates'][0]
            else:
                upd = update
            type = self.get_update_type(update)
            if type == 'message_chat_created':
                st_payload = upd['start_payload']
        return st_payload

    def get_construct_text(self, update):
        text = self.get_text(update)
        return text

    def get_construct_attach(self, update):
        attach = self.get_attachments(update)
        return attach

    def get_construct_attach_type(self, update):
        att_type = self.get_attach_type(update)
        return att_type

    def get_construct_payload(self, update):
        payload = self.get_payload(update)
        return payload

    def edit_message(self, message_id, text, attachments=None, link=None, notify=True, format=None):
        update = None
        method = 'messages'
        params = (
            ('access_token', self.token),
            ('message_id', message_id),
        )
        data = {
            "text": text,
            "attachments": attachments,
            "link": link,
            "notify": notify,
            "format": format
        }
        flag = 'attachment.not.ready'
        while flag == 'attachment.not.ready':
            try:
                response = requests.put(self.url + method, params=params, data=json.dumps(data))
                upd = response.json()
                if 'code' in upd.keys():
                    flag = upd.get('code')
                    logger.info('ждем 5 сек...')
                else:
                    flag = None
                    if response.status_code == 200:
                        update = response.json()
                    else:
                        logger.error("Error edit message: {}".format(response.status_code))
            except Exception as e:
                logger.error("Error edit_message: %s.", e)
        return update

    def pin_message(self, chat_id, message_id, notify=True):
        update = None
        method = 'chats/{}'.format(chat_id) + '/pin'
        params = (('access_token', self.token),)
        data = {
            "message_id": message_id,
            "notify": notify
        }
        try:
            response = requests.put(self.url + method, params=params, data=json.dumps(data))
            upd = response.json()
            if 'message' in upd.keys():
                logger.info("pin impossible: {}".format(upd.get('message')))
            if 'success' in upd.keys():
                update = upd.get('success')
        except Exception as e:
            logger.error("Error pin_message: %s.", e)
        return update

    def unpin_message(self, chat_id):
        res = None
        method = 'chats/{}'.format(chat_id) + '/pin'
        params = {
            "access_token": self.token
        }
        try:
            res = requests.delete(self.url + method, params=params)
            res = res.json()
            if 'message' in res.keys():
                logger.info("unpin impossible: {}".format(res.get('message')))
            if 'success' in res.keys():
                res = res.get('success')
        except Exception as e:
            logger.error("Error unpin_message: %s.", e)
        return res

    def get_pinned_message(self, chat_id):
        message = None
        method = 'chats/{}'.format(chat_id) + '/pin'
        params = {
            "access_token": self.token
        }
        try:
            response = requests.get(self.url + method, params)
            message = response.json()
        except Exception as e:
            logger.error("Error connect get pinned message: %s.", e)
        return message

    def typing_on(self, chat_id):
        method_ntf = 'chats/{}'.format(chat_id) + '/actions?access_token='
        params = {"action": "typing_on"}
        try:
            requests.post(self.url + method_ntf + self.token, data=json.dumps(params))
        except Exception as e:
            logger.error("Error typing_on: %s.", e)

    def mark_seen(self, chat_id):
        method_ntf = 'chats/{}'.format(chat_id) + '/actions?access_token='
        params = {"action": "mark_seen"}
        try:
            requests.post(self.url + method_ntf + self.token, data=json.dumps(params))
        except Exception as e:
            logger.error("Error connect in mark_seen: %s.", e)

    def sending_video(self, chat_id):
        method_ntf = 'chats/{}'.format(chat_id) + '/actions?access_token='
        params = {"action": "sending_video"}
        try:
            requests.post(self.url + method_ntf + self.token, data=json.dumps(params))
        except Exception as e:
            logger.error("Error sending_video: %s.", e)

    def sending_audio(self, chat_id):
        method_ntf = 'chats/{}'.format(chat_id) + '/actions?access_token='
        params = {"action": "sending_audio"}
        try:
            requests.post(self.url + method_ntf + self.token, data=json.dumps(params))
        except Exception as e:
            logger.error("Error sending_audio: %s.", e)

    def sending_photo(self, chat_id):
        method_ntf = 'chats/{}'.format(chat_id) + '/actions?access_token='
        params = {"action": "sending_photo"}
        try:
            requests.post(self.url + method_ntf + self.token, data=json.dumps(params))
        except Exception as e:
            logger.error("Error sending_photo: %s.", e)

    def sending_image(self, chat_id):
        method_ntf = 'chats/{}'.format(chat_id) + '/actions?access_token='
        params = {"action": "sending_image"}
        try:
            requests.post(self.url + method_ntf + self.token, data=json.dumps(params))
        except Exception as e:
            logger.error("Error sending_image: %s.", e)

    def sending_file(self, chat_id):
        method_ntf = 'chats/{}'.format(chat_id) + '/actions?access_token='
        params = {"action": "sending_file"}
        try:
            requests.post(self.url + method_ntf + self.token, data=json.dumps(params))
        except Exception as e:
            logger.error("Error sending_file: %s.", e)

    def delete_message(self, message_id):
        method = 'messages'
        params = {
            "message_id": message_id,
            "access_token": self.token
        }
        try:
            requests.delete(self.url + method, params=params)
        except Exception as e:
            logger.error("Error delete_message: %s.", e)

    def attach_buttons(self, buttons):
        # self.typing_on(self.get_chat_id())
        attach = None
        if isinstance(buttons, list):
            try:
                if buttons[0][0]:
                    attach = [{"type": "inline_keyboard",
                               "payload": {"buttons": buttons}
                               }
                              ]
            except Exception as e:
                attach = [{"type": "inline_keyboard",
                           "payload": {"buttons": [buttons]}
                           }
                          ]
                logger.info('atach_button is list, except (%s)', e)
        else:
            attach = [{"type": "inline_keyboard",
                       "payload": {"buttons": [[buttons]]}
                       }
                      ]
        return attach

    def button_callback(self, text, payload, intent='default'):
        button = {"type": 'callback',
                  "text": text,
                  "payload": payload,
                  "intent": intent}
        return button

    def button_link(self, text, url):
        button = {"type": 'link',
                  "text": text,
                  "url": url}
        return button

    def button_contact(self, text):
        button = {"type": 'request_contact',
                  "text": text}
        return button

    def button_location(self, text, quick=False):
        button = {"type": 'request_geo_location',
                  "text": text,
                  "quick": quick}
        return button

    def button_chat(self, text, chat_title, chat_description=None, start_payload=None, uuid=None):
        button = {"type": 'chat',
                  "text": text,
                  "chat_title": chat_title,
                  "chat_description": chat_description,
                  "start_payload": start_payload,
                  "uuid": uuid}
        return button

    def send_buttons(self, text, buttons, chat_id, format=None):
        # self.typing_on(chat_id)
        attach = self.attach_buttons(buttons)
        update = self.send_message(text, chat_id, attachments=attach, format=format)
        return update

    def upload_url(self, type):
        url = None
        method = 'uploads'
        params = (
            ('access_token', self.token),
            ('type', type),
        )
        try:
            response = requests.post(self.url + method, params=params)
            if response.status_code == 200:
                update = response.json()
                url = update.get('url')
        except Exception as e:
            logger.error("Error upload_url: %s.", e)
        return url

    def markup(self, type, from_posit, length):
        markup = [{"type": type,
                  "from": from_posit,
                  "length": length}]
        return markup

    def attach_file(self, content, content_name=None):
        self.sending_file(self.get_chat_id())
        token = self.token_upload_content('file', content, content_name)
        attach = [{"type": "file", "payload": token}]
        return attach

    def send_file(self, content, chat_id, text=None, content_name=None, format=None):
        self.sending_file(chat_id)
        attach = self.attach_file(content, content_name)
        update = self.send_message(text, chat_id, attachments=attach, format=format)
        return update

    def attach_image(self, content):
        self.sending_photo(self.get_chat_id())
        attach = []
        if isinstance(content, str):
            token = self.token_upload_content('image', content)
            attach.append({"type": "image", "payload": token})
        else:
            for cont in content:
                token = self.token_upload_content('image', cont)
                attach.append({"type": "image", "payload": token})
        return attach

    def send_image(self, content, chat_id, text=None, format=None):
        self.sending_photo(chat_id)
        attach = self.attach_image(content)
        update = self.send_message(text, chat_id, attachments=attach, format=format)
        return update

    def attach_image_url(self, url):
        self.sending_photo(self.get_chat_id())
        attach = []
        if isinstance(url, str):
            attach.append({"type": "image", "payload": {'url': url}})
        else:
            for cont in url:
                attach.append({"type": "image", "payload": {'url': cont}})
        return attach

    def send_image_url(self, url, chat_id, text=None, format=None):
        self.sending_photo(chat_id)
        attach = self.attach_image_url(url)
        update = self.send_message(text, chat_id, attachments=attach, format=format)
        return update

    def attach_video(self, content):
        self.sending_video(self.get_chat_id())
        attach = []
        if isinstance(content, str):
            token = self.token_upload_content('video', content)
            attach.append({"type": "video", "payload": token})
        else:
            for cont in content:
                token = self.token_upload_content('video', cont)
                attach.append({"type": "video", "payload": token})
        return attach

    def send_video(self, content, chat_id, text=None, format=None):
        self.sending_video(chat_id)
        attach = self.attach_video(content)
        update = self.send_message(text, chat_id, attachments=attach, format=format)
        return update

    def attach_audio(self, content):
        token = self.token_upload_content('audio', content)
        attach = [{"type": "audio", "payload": token}]
        return attach

    def send_audio(self, content, chat_id, text=None, format=None):
        self.sending_audio(chat_id)
        attach = self.attach_audio(content)
        update = self.send_message(text, chat_id, attachments=attach, format=format)
        return update

    def send_forward_message(self, text, mid, chat_id, user_id=None, format=None):
        # self.typing_on(chat_id)
        link = self.link_forward(mid)
        update = self.send_message(text, chat_id, user_id, link=link, format=format)
        return update

    def link_reply(self, mid):
        link = {"type": "reply",
                "mid": mid
                }
        return link

    def link_forward(self, mid):
        link = {"type": "forward",
                "mid": mid
                }
        return link

    def send_reply_message(self, text, mid, chat_id, dislinkprev=None, format=None):
        # self.typing_on(chat_id)
        link = self.link_reply(mid)
        update = self.send_message(text, chat_id, link=link, dislinkprev=dislinkprev, format=format)
        return update

    def token_upload_content(self, type, content, content_name=None):
        token = None
        url = self.upload_url(type)
        if content_name is None:
            content_name = os.path.basename(content)
        try:
            content = open(content, 'rb')
        except Exception as e:
            logger.error("Error upload file (no such file): %s", e)
        try:
            response = requests.post(url, files={'files': (content_name, content, 'multipart/form-data')})
            if response.status_code == 200:
                token = response.json()
        except Exception as e:
            logger.error("Error token_upload_content: %s.", e)
        return token

    def send_message(self, text, chat_id, user_id=None, attachments=None, link=None, notify=True, dislinkprev=False, format=None):
        self.typing_on(chat_id)
        update = None
        method = 'messages'
        params = (
            ('access_token', self.token),
            ('chat_id', chat_id),
            ('user_id', user_id),
            ('disable_link_preview', dislinkprev)
        )
        data = {
            "text": text,
            "attachments": attachments,
            "link": link,
            "notify": notify,
            "format": format
        }
        flag = 'attachment.not.ready'
        while flag == 'attachment.not.ready':
            try:
                response = requests.post(self.url + method, params=params, data=json.dumps(data))
                upd = response.json()
                if 'code' in upd.keys():
                    flag = upd.get('code')
                    logger.info('send_message: attach not ready, wait 5s')
                else:
                    flag = None
                    if response.status_code == 200:
                        update = response.json()
                        logger.info('send_message: OK')
                    else:
                        logger.error("Error sending message: {}".format(response.status_code))
            except Exception as e:
                logger.error("Error send_message: %s.", e)
        return update

    def send_answer_callback(self, callback_id, notification, text=None, attachments=None, link=None, notify=True, format=None):
        update = None
        method = 'answers'
        params = (
            ('access_token', self.token),
            ('callback_id', callback_id),
        )
        message = {"text": text,
                   "attachments": attachments,
                   "link": link,
                   "notify": notify,
                   "format": format
                   }
        if text is None and attachments is None and link is None:
            message = None
        data = {
            "message": message,
            "notification": notification
        }
        flag = 'attachment.not.ready'
        while flag == 'attachment.not.ready':
            try:
                response = requests.post(self.url + method, params=params, data=json.dumps(data))
                upd = response.json()
                if 'code' in upd.keys():
                    flag = upd.get('code')
                    logger.info('انتظر 5 ثواني')
                    time.sleep(5)
                else:
                    flag = None
                    if response.status_code == 200:
                        update = response.json()
                    else:
                        logger.error("Error answer callback: {}".format(response.status_code))
            except Exception as e:
                logger.error("Error answer_callback: %s.", e)
        return update

    def send_construct_message(self, session_id, hint, text=None, attachments=None, markup=None, format=None,
                               allow_user_input=True, data=None, buttons=None, placeholder=None):
        update = None
        method = 'answers/constructor'
        params = (
            ('access_token', self.token),
            ('session_id', session_id),
        )
        message = [{"text": text,
                    "attachments": attachments,
                    "markup": markup,
                    "format": format
                    }]
        if text is None:
            message = []
        if buttons is None:
            buttons = []
        keyboard = {"buttons": buttons}

        datas = {
            "messages": message,
            "allow_user_input": allow_user_input,
            "hint": hint,
            "data": data,
            "keyboard": keyboard,
            "placeholder": placeholder
        }
        flag = 'attachment.not.ready'
        while flag == 'attachment.not.ready':
            try:
                response = requests.post(self.url + method, params=params, data=json.dumps(datas))
                upd = response.json()
                if 'code' in upd.keys():
                    flag = upd.get('code')
                    logger.info('send_construct_message: انتظر 5 ثواني...')
                    time.sleep(5)
                else:
                    flag = None
                    if response.status_code == 200:
                        update = response.json()
                        logger.info('send_construct_message: OK')
                    else:
                        logger.error("Error construct_message: {}".format(response.status_code))
            except Exception as e:
                logger.error("Error construct_message: %s.", e)
        return update
