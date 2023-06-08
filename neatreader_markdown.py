import json

class Note:
    def __init__(self, text, note):
        self.text = text
        self.note = note

def main():
    json_str = """{"bookName":"Java Coding Problems (Anghel Leonard) (Z-Library)","noteList":[{"guid":"0924697d-55c4-49e1-abcb-835d9e26bd2f","spineIndex":209,"startCharIndex":514,"endCharIndex":754,"color":1,"text":"public static void reverse(int[] arr) {\n\n  for (int leftHead = 0, rightHead = arr.length - 1; \n      leftHead < rightHead; leftHead++, rightHead--) {\n\n    int elem = arr[leftHead];\n    arr[leftHead] = arr[rightHead];\n    arr[rightHead] = elem;\n  }\n}","note":"code","updateTime":1686217935483,"time":"2023-06-08 17:52","bgColor":"#FFED6C","showTime":"2023-06-08 17:52:15"},{"guid":"2725065e-d95d-4f63-8e15-653c9ba20788","spineIndex":209,"startCharIndex":349,"endCharIndex":514,"color":4,"text":"Let's start with a simple implementation that swaps the first element of the array with the last element, the second element with the penultimate element, and so on:","note":"","updateTime":1686217925248,"time":"2023-06-08 17:52","bgColor":"#C3F172","showTime":"2023-06-08 17:52:05"},{"guid":"c7c1163c-1827-4c38-b41b-5dd0b5911790","spineIndex":209,"startCharIndex":754,"endCharIndex":950,"color":4,"text":"The preceding solution mutates the given array and this is not always the desired behavior. Of course, we can modify it to return a new array, or we can rely on Java 8 functional style as follows:","note":"测试笔记2","updateTime":1686216179473,"time":"2023-06-08 17:22","bgColor":"#C3F172","showTime":"2023-06-08 17:22:59"}]}"""
    json_str = json_str.replace("\n", "\\n")
    
    data = json.loads(json_str)
    note_list = [Note(note['text'], note['note']) for note in data['noteList']]
    markdown = f"# {data['bookName']}\n\n"
    for note in reversed(note_list):
        if note.note == "code":
            markdown += f"```java\n{note.text}\n```\n\n"
        else:
            markdown += f"{note.text}\n\n"
        if note.note and note.note != "code":
            markdown += f"> {note.note}\n\n"
        markdown += "---\n"

    
    with open(f"{data['bookName']}.md", "w", encoding="utf-8") as f:
        f.write(markdown)

if __name__ == "__main__":
    main()
