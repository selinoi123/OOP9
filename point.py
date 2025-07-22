import math
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value

    def __repr__(self):
        return f"Point({self.__x}, {self.__y})"

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        return False

    def __hash__(self):
        return hash((self.__x, self.__y))


p1 = Point(3, 4)
p2 = Point(3, 4)


value1 = math.sqrt(p1.get_x() ** 2 + p1.get_y() ** 2)

points_dict = {}
points_dict[p1] = value1

# ניסיון להכניס מפתח חדש שהוא p2, עם ערך מחרוזתי
points_dict[p2] = "point"

# הדפסת התוצאה
for key, value in points_dict.items():
    print(f"{key}: {value}")


# שאלה מס 1
# רק פריט אחד מאוחסן כיוון שp1 וp2 שווים מבחינת הלוגית וניתן גם לראות שהפונקרציה ep מחזירה True כלומר ממחישה את זה שהם שווים זה לזה
# בנוסף האובייקטים צריכים להיות יחודיים

#2
#התנגשות גיבוב זה מצב שבו שני אובייקטים שונים מייצרים את אותו גיבוב , למרות שהם לא שווים .
#בקוד הספציפי הזה לא, מכיוון שp1ן p2לא רק יש את אותו הגיבוב, הם גם שווים מבחינת התוכן.

#3
# ספירת ההפניות זה שכל אובייקט עוקב אחר מספר ההפניות המצביעות אליו אבל כאשר אין פניות לאותו אובייקט
# כלומר אין בו שימוש יהיה אפשר למחוק אותו מבלי שיפגע הקוד
# בנוסף יש קשר לאיסוף הזבל כי הפייתון מחזיר לעצמו את הזיכרון, ומפנה אותו לשימוש אחר