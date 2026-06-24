import streamlit as st
import json
import os
from questions import LEVEL_1, LEVEL_2, LEVEL_3, LEVEL_4, LEVEL_5

USERS_FILE = "users.json"
PROGRESS_FILE = "progress.json"

# إنشاء الملفات إذا لم تكن موجودة
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)

if not os.path.exists(PROGRESS_FILE):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump({}, f)

# دوال مساعدة
def load_users():
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

def load_progress():
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_progress(data):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# إعداد الصفحة
st.set_page_config(
    page_title="بطل السكري",
    page_icon="⭐",
    layout="centered"
)
st.markdown("""
<style>
.stApp{
    background-color:#DFF6FF;
}
h1,h2,h3{
    text-align:center;
    color:#1E3A8A !important;
}
p,div,span,label{
    color:#111827 !important;
}
.stButton>button{
    border-radius:15px;
    height:50px;
    font-size:18px;
}
</style>
""", unsafe_allow_html=True)
st.title("⭐ بطل السكري")

# الجلسة
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

# قبل تسجيل الدخول
if not st.session_state.logged_in:

    menu = st.sidebar.selectbox(
        "القائمة",
        ["الرئيسية", "تسجيل مستخدم", "تسجيل دخول"]
    )

    if menu == "الرئيسية":
        st.header("مرحباً بك في بطل السكري")
        st.write("""
        تطبيق تعليمي للأطفال المصابين بالسكري.

        ✅ تعلم بطريقة ممتعة
        ✅ مستويات تعليمية
        ✅ شارات وإنجازات
        ✅ متابعة التقدم
        """)

    elif menu == "تسجيل مستخدم":

        st.header("إنشاء حساب جديد")

        username = st.text_input("اسم المستخدم")
        password = st.text_input("كلمة المرور", type="password")
        child_name = st.text_input("اسم الطفل")
        age = st.number_input("العمر", 1, 18)

        role = st.selectbox(
            "نوع الحساب",
            ["طفل", "ولي أمر"]
        )

        linked_child = ""

        if role == "ولي أمر":
            linked_child = st.text_input(
                "اسم مستخدم الطفل"
            )

        if st.button("إنشاء الحساب"):

            users = load_users()

            exists = any(
                u["username"] == username
                for u in users
            )

            if exists:
                st.error("اسم المستخدم مستخدم مسبقاً")

            else:

                users.append({
                    "username": username,
                    "password": password,
                    "child_name": child_name,
                    "age": age,
                    "role": role,
                    "linked_child": linked_child
                })

                save_users(users)

                st.success("تم إنشاء الحساب بنجاح")
                                

    elif menu == "تسجيل دخول":


    

        st.header("تسجيل الدخول")

        username = st.text_input("اسم المستخدم")
        password = st.text_input("كلمة المرور", type="password")

        if st.button("دخول"):

            users = load_users()

            user = None

            for u in users:
                if (
                    u["username"] == username
                    and u["password"] == password
                ):
                    user = u
                    break

            if user:
                st.session_state.logged_in = True
                st.session_state.user = user
                st.rerun()

            else:
                st.error("بيانات الدخول غير صحيحة")

# دالة عرض أي مستوى
def show_level(level_name, questions, user):

    st.header(f"📚 {level_name}")

    answers = []

    for i, q in enumerate(questions):
        answer = st.radio(
    q["question"],
    q["options"],
    index=None,
    key=f"{level_name}_{i}"
)
        answers.append(answer)

    if st.button(f"إنهاء {level_name}"):

        correct = 0

        for ans, q in zip(answers, questions):
            if ans == q["answer"]:
                correct += 1

        score = int((correct / len(questions)) * 100)

        progress = load_progress()

        if user["username"] not in progress:
            progress[user["username"]] = {}

        progress[user["username"]][level_name] = score

        save_progress(progress)

        st.success(f"درجتك {score}%")

        if score >= 80:
            st.balloons()
            st.success("🏆 أحسنت! حصلت على الشارة")


# بعد تسجيل الدخول
# بعد تسجيل الدخول
if st.session_state.logged_in:

    user = st.session_state.user
    role = user.get("role", "طفل")

    # ==================
    # لوحة ولي الأمر
    # ==================
    if role == "ولي أمر":

        st.header("👩 لوحة ولي الأمر")

        progress = load_progress()

        child_username = user.get(
            "linked_child",
            ""
        )

        user_progress = progress.get(
            child_username,
            {}
        )

        st.write(
            f"👦 اسم الطفل: {child_username}"
        )

        if user_progress:

            for level, score in user_progress.items():

                st.write(f"{level}: {score}%")
                st.progress(score / 100)

            avg = int(
                sum(user_progress.values())
                / len(user_progress)
            )

            st.metric(
                "التقدم العام",
                f"{avg}%"
            )

        else:
            st.info("لا توجد نتائج بعد")

        if st.button("تسجيل خروج"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.rerun()

    # ==================
    # واجهة الطفل
    # ==================
    else:

        st.sidebar.success(
            f"مرحباً {user['child_name']} 🦸"
        )

        progress = load_progress()

        user_progress = progress.get(
            user["username"],
            {}
        )

        options = [
            "لوحة الطفل",
            "المستوى الأول"
        ]

        if user_progress.get("المستوى الأول", 0) >= 80:
            options.append("المستوى الثاني")

        if user_progress.get("المستوى الثاني", 0) >= 80:
            options.append("المستوى الثالث")

        if user_progress.get("المستوى الثالث", 0) >= 80:
            options.append("المستوى الرابع")

        if user_progress.get("المستوى الرابع", 0) >= 80:
            options.append("المستوى الخامس")

        options.append("تسجيل خروج")

        page = st.sidebar.selectbox(
            "اختر",
            options
        )

        if page == "لوحة الطفل":

            st.header("🏆 لوحة الطفل")

            score1 = user_progress.get("المستوى الأول", 0)
            score2 = user_progress.get("المستوى الثاني", 0)
            score3 = user_progress.get("المستوى الثالث", 0)
            score4 = user_progress.get("المستوى الرابع", 0)
            score5 = user_progress.get("المستوى الخامس", 0)

            total = int(
                (score1 + score2 + score3 + score4 + score5) / 5
            )

            st.metric(
                "التقدم العام",
                f"{total}%"
            )

            st.progress(total / 100)

        elif page == "المستوى الأول":
            show_level("المستوى الأول", LEVEL_1, user)

        elif page == "المستوى الثاني":
            show_level("المستوى الثاني", LEVEL_2, user)

        elif page == "المستوى الثالث":
            show_level("المستوى الثالث", LEVEL_3, user)

        elif page == "المستوى الرابع":
            show_level("المستوى الرابع", LEVEL_4, user)

        elif page == "المستوى الخامس":
            show_level("المستوى الخامس", LEVEL_5, user)

        elif page == "تسجيل خروج":

            st.session_state.logged_in = False
            st.session_state.user = None
            st.rerun()