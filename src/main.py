import random

from flask import Flask, request, jsonify

from src.announcement import Announcement

api=Flask(__name__)

announcements: [Announcement] = []

@api.route('/announcements', methods=['GET'])
def getAnnouncements():
    result = []
    for announcement in announcements:
        item = {}
        item["id"] = announcement.id
        item["title"] = announcement.title
        item["text"] = announcement.text
        result.append(item)

    return jsonify(result), 200


@api.route('/announcement/<int:id>', methods=['GET'])
def getAnnouncement(id):
    result = []
    for announcement in announcements:
        if announcement.id == id:
            result.append({
                "title":  announcement.title,
                "text": announcement.text
            })

    return jsonify(result), 200

@api.route('/insert', methods=['POST'])
def insert():
    title = request.form["title"]
    text = request.form["text"]

    announcement = Announcement(random.sample(range(100), 10), title)
    announcement.change_text(text)
    announcements.append(announcement)
    return 200

@api.route('/update', methods=['PUT'])
def update():
    title = request.form["title"]
    newText = request.form["newText"]
    for announcement in announcements:
        if announcement.title == title:
            announcement.change_text(newText)
    return 200

@api.route('/delete', methods=['DELETE'])
def delete():
    title = request.form["title"]
    for announcement in announcements:
        if announcement.title == title:
            announcements.remove(announcement)
    return 200

if __name__ == '__main__':
    api.run('127.0.0.1', 8888)