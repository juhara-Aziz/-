import streamlit as st

st.title("تطبيق متابعة السكر")


#تسجيل مستخدم جديد
with open("children.txt","a") as file:
  pass

def register_user():
    #ادخال بيانات المستخدم


    st.title("\n" + "=" * 40)
    st.title("تسجيل مستخدم جديد")
    st.title("=" * 40)

    username = st.text_input("اسم المستخدم: ")
    password = st.text_input("كلمة المرور: ")
    child_name = st.text_input("اسم الطفل: ")
    age = int(st.text_input("عمر الطفل: "))
    gender = st.text_input("جنس الطفل: ")

#التحقق من تكرار اسم المستخدم
    found = False

    with open("children.txt","r") as file:

     for line in file:
      data = line.strip().split(",")

      if username==data[0]:
        found=True

#اذا اسم المستخدم مسجل سابقا

    if found:
      st.title("\nاسم المستخدم مستخدم مسبقاً، يرجى اختيار اسم مستخدم آخر.")

#اذا اسم المستخدم غير مسجل مسبقا

    else:
      child={
        "username":username,
        "password":password,
        "name":child_name,
        "age":age,
        "gender":gender
           }

#حفظ البيانات في الملف
    with open("children.txt","a") as file:

      file.write(
        f"{username},{password},{child_name},{age},{gender}\n" )

      st.title(f"\nتم إنشاء حساب الطفل {child_name} بنجاح.")
    return child

#----------------------------------------------------------------
#تسجيل الدخول ولي الأمر

def login_parent():

    st.title("\n" + "=" * 40)
    st.title("تسجيل الدخول")
    st.title("=" * 40)

    username = st.text_input("اسم المستخدم: ")
    password = st.text_input("كلمة المرور: ")

    found = False

    with  open("children.txt","r") as file:

     for line in file:
      data = line.strip().split(",")

      if username==data[0]and password==data[1]:
        found=True
        break


    if found:

     st.title("\nتم تسجيل الدخول بنجاح.")

     child = {
        "username": data[0],
        "password": data[1],
        "name": data[2],
        "age": data[3],
        "gender": data[4]
     }
     return child

    else:
     st.title("\nاسم المستخدم أو كلمة المرور غير صحيحة.")
     return None
 #----------------------------------------------------------------
 # تسجيل الطفل
def login_child():

  st.title("\n" + "=" * 40)
  st.title("تسجيل الدخول")
  st.title("=" * 40)

  username = st.text_input("اسم المستخدم: ")
  password = st.text_input("كلمة المرور: ")

  found = False

  with open("children.txt","r") as file:

   for line in file:
    data = line.strip().split(",")

    if username==data[0]and password==data[1]:
      found=True
      break

  if found:
   child = {
    "username": data[0],
    "password": data[1],
    "name": data[2],
    "age": data[3],
    "gender": data[4]
   }

   st.title(f"\nمرحباً   {child['name']}!")
   st.title("جاري الانتقال إلى المستويات...")
   return child


  else:
    st.title("\nاسم المستخدم أو كلمة المرور غير صحيحة.")
    return None
#----------------------------------------------------------------
#تعريف الدرجات والشارات التي يصل عليها الطفل
score = 0
titles =[]

def level_1(child_name):

    score = 0

    print("=" * 50)
    print("المستوى الأول: العادات الصحية")
    print("=" * 50)
    print(f"""
مرحباً {child_name}، اليوم سنتعلم كيف نحافظ على صحتنا بتعلم العادات الصحية،
وسنحصل على شارة جديدة! هيا بنا.
""")

    st.text_input("اضغط Enter للبدء...")

    questions = [

        {
            "question": "هل السكري يمنعني من اللعب مع أصدقائي؟",
            "choices": [
                "نعم",
                "لا، أستطيع اللعب مع تنظيم صحتي"
            ],
            "answer": 2
        },

        {
            "question": "هل آكل طوال اليوم؟",
            "choices": [
                "نعم",
                "لا، آكل في أوقات الوجبات"
            ],
            "answer": 2
        },

        {
            "question": "إذا شعرت بالجوع ....",
            "choices": [
                "أخبر بابا وماما",
                "آكل أي شيء"
            ],
            "answer": 1
        },

        {
            "question": "قبل أن آكل ....",
            "choices": [
                "أخبر بابا وماما",
                "آكل مباشرة"
            ],
            "answer": 1
        },

        {
            "question": "يجب عليك دائماً الحرص على شرب ....",
            "choices": [
                "العصائر",
                "الماء"
            ],
            "answer": 2
        }

    ]

    # ===== الأسئلة =====

    for q in questions:

        st.title("\n" + q["question"])

        for i, choice in enumerate(q["choices"], start=1):
            st.title(f"{i}. {choice}")

        while True:
            try:
                user = int(st.text_input("اختر الإجابة: "))
                if user in [1, 2]:
                    break
                st.title("الرجاء اختيار 1 أو 2 فقط.")
            except ValueError:
                st.title("الرجاء إدخال رقم صحيح.")

        if user == q["answer"]:

            st.title("⭐ إجابة صحيحة!")
            score += 20

        else:

            st.title("❌ إجابة خاطئة!")

            correct = q["choices"][q["answer"] - 1]

            st.title(f"✅ الإجابة الصحيحة: {correct}")

    # ===== النتيجة =====

    st.title("\n" + "=" * 50)
    st.title(f"⭐ درجتك هي: {score}/100")

    with open("progress.txt", "a", encoding="utf-8") as file:
        file.write(f"Level 1:{score}\n")

    if score >= 80:

        st.title(f"\n🎉 ممتاز يا {child_name}!")
        st.title("🏅 لقد حصلت على شارة جديدة!")
        st.title("🏅 بطل العادات الصحية")
        st.title("\nلنذهب إلى المستوى الثاني")

        return score, "بطل العادات الصحية"

    else:

        st.title("\n💪 محاولة جيدة")
        st.title("لكن لنلعب بشكل أفضل المرة القادمة، حسناً؟")

        return score, None


def level_2(child_name):

    score = 0

    st.title("=" * 50)
    st.title("المستوى الثاني: اختر طعامك")
    st.title("=" * 50)

    st.title(f"""
مرحباً يا {child_name}!

الكربوهيدرات تعطينا الطاقة لنلعب ونتعلم.
لكن تناول كمية كبيرة منها دون حساب قد يرفع مستوى السكر.

هيا نتعلم كيف نكون أبطالاً في حساب الكربوهيدرات!
""")

    st.text_input("اضغط Enter للبدء...")

    questions = [

        {
            "question": "الكربوهيدرات هي ....",
            "choices": [
                "طاقة تساعدني على اللعب والحركة ⚡",
                "اكل غير جيد"
            ],
            "answer": 1
        },

        {
            "question": "إذا أكلت كمية كبيرة جداً من الكربوهيدرات دون حساب، ماذا قد يحدث؟",
            "choices": [
                "قد يرتفع مستوى السكر 📈",
                "سأصبح أطول فوراً 😄"
            ],
            "answer": 1
        },

        {
            "question": "أين أجد الكربوهيدرات غالباً؟",
            "choices": [
                "في الخبز والأرز والمعكرونة 🍞🍚🍝",
                "في كل الطعام"
            ],
            "answer": 1
        },

        {
            "question": "أيهما أفضل كوجبة خفيفة؟",
            "choices": [
                "تفاحة 🍎",
                "عدة قطع كبيرة من الحلوى 🍬🍬🍬"
            ],
            "answer": 1
        },

        {
            "question": "أيهما أفضل لبطل السكري؟",
            "choices": [
                "ماما وبابا يحسبون لي الكاربوهيدرات",
                "أكل أي كمية دون حساب"
            ],
            "answer": 1
        }

    ]

    for q in questions:

        st.title("\n" + q["question"])

        for i, choice in enumerate(q["choices"], start=1):
            st.title(f"{i}. {choice}")

        while True:
            try:
                user = int(st.text_input("اختر الإجابة: "))

                if user in [1, 2]:
                    break

                st.title("اختر 1 أو 2 فقط.")

            except ValueError:
                st.title("الرجاء إدخال رقم صحيح.")

        if user == q["answer"]:

            st.title("⭐ إجابة صحيحة!")
            score += 20

        else:

            st.title("❌ إجابة خاطئة!")

            correct = q["choices"][q["answer"] - 1]

            st.title(f"✅ الإجابة الصحيحة: {correct}")

    st.title("\n" + "=" * 50)
    st.title(f"⭐ درجتك هي: {score}/100")

    with open("progress.txt", "a", encoding="utf-8") as file:
        file.write(f"Level 2:{score}\n")

    if score >= 80:

        st.title(f"\n🎉 رائع يا {child_name}!")
        st.title("🏅 لقد حصلت على شارة جديدة!")
        st.title("🏅 بطل الكربوهيدرات الذكي")

        return score, "بطل الكربوهيدرات الذكي"

    else:

        st.title("\n💪 محاولة جيدة!")
        st.title("هيا نجرب مرة أخرى لنحصل على الشارة.")

        return score, None


#############
def level_3(child_name):

    score = 0

    st.title("=" * 50)
    st.title("المستوى الثالث: بطل القرار الصحيح")
    st.title("=" * 50)

    st.title(f"""
مرحباً يا {child_name}!

أحياناً نواجه مواقف مفاجئة في المدرسة أو المنزل أو أثناء الخروج.
في هذا المستوى سنتعلم كيف نتخذ القرار الصحيح لنحافظ على صحتنا.

هيا نبدأ!
""")

    st.text_input("اضغط Enter للبدء...")

    questions = [

        {
            "question": "في المدرسة أعطاك صديقك حلوى 🍬، ماذا تفعل؟",
            "choices": [
                "أسأل المعلم أو أتواصل مع أهلي قبل أكلها",
                "آكلها مباشرة"
            ],
            "answer": 1
        },

        {
            "question": "وجدت عصيراً في الثلاجة 🧃، ماذا تفعل؟",
            "choices": [
                "أسأل إذا كان مناسباً لي وكمية الكربوهيدرات فيه",
                "أشربه كله مباشرة"
            ],
            "answer": 1
        },

        {
            "question": "في العيد كانت هناك الكثير من الحلويات 🍭🍫، ماذا تفعل؟",
            "choices": [
                "أختار كمية مناسبة وأخبر أهلي",
                "آكل كل ما أستطيع"
            ],
            "answer": 1
        },

        {
            "question": "في المطعم أحضرت القائمة 🍔🍟، ماذا تفعل أولاً؟",
            "choices": [
                "أختار وجبة مناسبة بمساعدة أهلي",
                "أطلب أكبر وجبة دون تفكير"
            ],
            "answer": 1
        },

        {
            "question": "كنت عند جدتي وقدمت لك وجبة جديدة 🍽️، ماذا تفعل؟",
            "choices": [
                "أسأل إذا كانت مناسبة لي وأخبر أهلي",
                "آكلها مباشرة"
            ],
            "answer": 1
        }

    ]

    for q in questions:

        st.title("\n" + q["question"])

        for i, choice in enumerate(q["choices"], start=1):
            st.title(f"{i}. {choice}")

        while True:
            try:
                user = int(st.text_input("اختر الإجابة: "))

                if user in [1, 2]:
                    break

                st.title("اختر 1 أو 2 فقط.")

            except ValueError:
                st.title("الرجاء إدخال رقم صحيح.")

        if user == q["answer"]:

            st.title("⭐ إجابة صحيحة!")
            score += 20

        else:

            st.title("❌ إجابة خاطئة!")

            correct = q["choices"][q["answer"] - 1]

            st.title(f"✅ الإجابة الصحيحة: {correct}")

            st.title("\n" + "=" * 50)
            st.title(f"⭐ درجتك هي: {score}/100")

            with open("progress.txt", "a", encoding="utf-8") as file:
              file.write(f"Level 3:{score}\n")

    if score >= 80:

        st.title(f"\n🎉 ممتاز يا {child_name}!")
        st.title("🏅 لقد حصلت على شارة جديدة!")
        st.title("🏅 بطل القرار الصحيح")

        return score, "بطل القرار الصحيح"

    else:

        st.title("\n💪 محاولة جيدة!")
        st.title("هيا نجرب مرة أخرى لنحصل على الشارة.")

        return score, None




###########
def level_4(child_name):
    score = 0

    st.title("=" * 50)
    st.title("المستوى الرابع: بطل الممارسات الصحية")
    st.title("=" * 50)

    st.title(f"""
{child_name}أحسنت يا !

الآن سنتعلم بعض الممارسات اليومية
التي تساعد أبطال السكري على المحافظة على صحتهم.
""")

    st.text_input("اضغط Enter للبدء...")

    questions = [
        {
            "question": "هل تساعد الحركة واللعب على المحافظة على الصحة؟",
            "choices": ["نعم 🏃", "لا"],
            "answer": 1
        },
        {
            "question": "هل النوم الجيد مهم لصحتي؟",
            "choices": ["نعم 😴", "لا"],
            "answer": 1
        },
        {
            "question": "إذا شعرت بتعب أو لم أشعر أنني بخير، ماذا أفعل؟",
            "choices": ["أخبر أهلي أو شخصاً بالغاً", "لا أخبر أحداً"],
            "answer": 1
        },
        {
            "question": "هل من الجيد أن أتبع تعليمات علاجي؟",
            "choices": ["نعم ✅", "لا"],
            "answer": 1
        },
        {
            "question": "أي عادة أفضل لبطل السكري؟",
            "choices": ["الحركة والنوم الجيد والطعام المناسب", "السهر وتجاهل صحتي"],
            "answer": 1
        }
    ]

    for q in questions:
        st.title("\n" + q["question"])
        for i, choice in enumerate(q["choices"], start=1):
            st.title(f"{i}. {choice}")

        try:
            user = int(st.text_input("اختر الإجابة (رقم): "))
            if user == q["answer"]:
                st.title("⭐ إجابة صحيحة!")
                score += 20
            else:
                st.title("❌ إجابة خاطئة!")
                st.title(f"✅ الإجابة الصحيحة هي: {q['choices'][q['answer'] - 1]}")
        except ValueError:
            st.title("❌ إدخال غير صالح! سيتم احتسابها إجابة خاطئة.")

    # نقلنا الطباعة للخارج لتكون بعد انتهاء كل الأسئلة
    st.title("\n" + "=" * 50)
    st.title(f"⭐ درجتك النهائية هي: {score}/100")

    with open("progress.txt", "a", encoding="utf-8") as file:
        file.write(f"Level 4:{score}\n")

    if score >= 80:
        st.title("\n🎉 ممتاز!")
        st.title("🏅 حصلت على شارة: بطل الممارسات الصحية")
        return score, "بطل الممارسات الصحية"
    else:
        st.title("\n💪 محاولة جيدة!")
        return score, None

##############
def level_5(child_name):

    score = 0

    st.title("=" * 50)
    st.title("المستوى الخامس: رحلة البطل")
    st.title("=" * 50)

    st.title(f"""
{child_name}مرحباً !

وصلت إلى المرحلة الأخيرة.

اليوم سنرافقك في رحلة كاملة،
ونرى هل أصبحت بطل السكري الحقيقي!
""")

    st.text_input("اضغط Enter للبدء...")

    questions = [

        {
            "question": f"استيقظ  صباحاً، ماذا يختار للإفطار؟",
            "choices": [
                "وجبة مناسبة مع معرفة الكربوهيدرات 🍳",
                "الكثير من الحلوى 🍬"
            ],
            "answer": 1
        },

        {
            "question": f"في المدرسة أعطى صديقٌ  قطعة حلوى، ماذا يفعل؟",
            "choices": [
                "يسأل شخصاً بالغاً أولاً",
                "يأكلها مباشرة"
            ],
            "answer": 1
        },

        {
            "question": f"حان وقت اللعب، ماذا يفعل؟",
            "choices": [
                "يلعب ويتحرك بنشاط ⚽",
                "يجلس طوال اليوم"
            ],
            "answer": 1
        },

        {
            "question": f"في زيارة عائلية وُجدت حلويات كثيرة، ماذا يفعل ؟",
            "choices": [
                "يختار كمية مناسبة",
                "يأكل كل الحلويات"
            ],
            "answer": 1
        },

        {
            "question": f"قبل النوم، ما أهم شيء يتذكره ؟",
            "choices": [
                "أن يهتم بصحته ويتبع العادات الصحيحة ❤️",
                "أن يتجاهل كل ما تعلمه"
            ],
            "answer": 1
        }

    ]

    for q in questions:

        st.title("\n" + q["question"])

        for i, choice in enumerate(q["choices"], start=1):
            st.title(f"{i}. {choice}")

        user = int(input("اختر الإجابة: "))

        if user == q["answer"]:
            st.title("⭐ إجابة صحيحة!")
            score += 20

        else:
            st.title("❌ إجابة خاطئة!")
            st.title(f"✅ الإجابة الصحيحة: {q['choices'][q['answer'] - 1]}")

    st.title("\n" + "=" * 50)
    st.title(f"⭐ درجتك هي: {score}/100")

    with open("progress.txt", "a", encoding="utf-8") as file:
        file.write(f"Level 5:{score}\n")

    if score >= 80:

        st.title(f"\n🎉{child_name} أحسنت يا !")
        st.title("🏅 لقد حصلت على الشارة الأخيرة!")
        st.title("👑 بطل السكري")

        return score, "بطل السكري"

    else:

        st.title("\n💪 اقتربت من الفوز بالشارة الأخيرة!")

        return score, None
#===============================================================
def total(child):

    total_score = 0
    titles = []

    score, badge = level_1(child["name"])
    total_score += score
    if badge:
        titles.append(badge)

    score, badge = level_2(child["name"])
    total_score += score
    if badge:
        titles.append(badge)

    score, badge = level_3(child["name"])
    total_score += score
    if badge:
        titles.append(badge)

    score, badge = level_4(child["name"])
    total_score += score
    if badge:
        titles.append(badge)

    score, badge = level_5(child["name"])
    total_score += score
    if badge:
        titles.append(badge)

    st.title("\n" + "=" * 50)
    st.title(f"🎉 تهانينا {child['name']}!")
    st.title(f"⭐ مجموع النقاط: {total_score}")

    st.title("\n🏅 الشارات التي حصلت عليها:")

    if titles:
        for title in titles:
            st.title("-", title)
    else:
        st.title("لم يتم الحصول على أي شارة")

    st.title("=" * 50)
#================================================================
#================================================================
import random

def parent_report(child):

    st.title("\n" + "=" * 50)
    st.title("📊 تقرير تقدم الطفل")
    st.title("=" * 50)

    st.title(f"👦 اسم الطفل: {child['name']}")
    st.title(f"🎂 العمر: {child['age']}")
    st.title(f"🧒 الجنس: {child['gender']}")
    st.title("\n📚 المستويات المكتملة:\n")

    scores = []

    performance = lambda score: "ممتاز 🌟" if score >= 90 else "جيد 👍" if score >= 70 else "يحتاج تحسين 💪"

    try:
        with open("progress.txt", "r", encoding="utf-8") as file:
            for line in file:

                data = line.strip().split(":")

                if len(data) != 2:
                    continue

                level_name = data[0]
                score = int(data[1])

                scores.append(score)

                status = performance(score)

                st.title(f"⭐ {level_name} → الدرجة: {score}/100 | التقييم: {status}")

        if len(scores) > 0:
            average = sum(scores) / len(scores)
            st.title(f"\n📈 متوسط الدرجات: {average:.2f}")
        else:
            st.title("لا يوجد تقدم مسجل بعد.")

    except FileNotFoundError:
        st.title("لا يوجد ملف تقدم حالياً.")

    tips = [
        "الالتزام بقياس السكر بانتظام يساعد على التحكم الأفضل بالسكري 🌟",
        "شرب الماء بانتظام عادة صحية مهمة لطفلك 💧",
        "النشاط البدني اليومي يساعد في الحفاظ على مستوى السكر ⚽",
        "احرص على توفير وجبات خفيفة صحية مثل الفواكه 🍎",
        "تعليم الطفل التعرف على أعراض انخفاض السكر مهم جداً 🚨",
        "الدعم النفسي والتشجيع يساعد الطفل على التعايش بثقة ❤️"
    ]

    daily_tip = random.choice(tips)

    st.title("\n💡 نصيحة اليوم:")
    st.title(daily_tip)

    st.title("=" * 50)
#----------------------------------------------------------------
#القائمة الرئيسية

st.titlet("=" * 40)
st.title("      بطل السكري")
st.title("=" * 40)

st.title("\nالقائمة الرئيسية")


st.title("1. تسجيل جديد")
st.title("2. تسجيل دخول")
st.title("3. خروج")

choice = st.text_input("\nاختر أحد الخيارات: ")
#----------------------------------------------------------------
#ولي الأمر

if choice in ["1", "١"]:

    st.title("\n" + "=" * 40)
    st.title("واجهة التسجيل ")
    st.title("=" * 40)

    #تسجيل جديد
    register_user()

 #----------------------------------------------------------------
 #تسجيل

elif choice in ["2","٢"]:

  st.title("1. ولي أمر")
  st.title("2. طفل")

  choice = st.text_input("\nاختر أحد الخيارات: ")

  if choice in ["1", "١"]:

    child = login_parent()

    if child:
        parent_report(child)

  elif choice in ["2","٢"]:
    child = login_child()

    if child:
     total(child)


#----------------------------------------------------------------
#خروج
elif choice in[ "3" ,"٣"]:
  st.title("\nشكراً لاستخدام تطبيق بطل السكري.")
  st.title("نتمنى لك يوماً سعيداً.")
#----------------------------------------------------------------
# خطأ بالاختيار
else:
  st.title("\nخيار غير صحيح، يرجى المحاولة مرة أخرى.")

