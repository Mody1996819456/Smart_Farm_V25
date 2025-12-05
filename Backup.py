import json
import time
from datetime import datetime

# --- 1. إعدادات وهيكل البيانات الأساسي ---

# اسم الملف الذي سيتم حفظ البيانات فيه
DATA_FILE = "farm_data.json"

# البيانات الأولية (تستخدم عند عدم العثور على ملف بيانات محفوظ)
initial_data = {
    "sectors": [
        {"id": "S1", "name": "القطاع الشمالي", "palms": 500, "trees": 200, "area": 50}
    ],
    "chemicals": [
        {"id": "C1", "name": "توباس", "type": "مبيد فطري", "stock": 100, "unit": "لتر", "threshold": 10},
        {"id": "C2", "name": "يوريا", "type": "سماد نيتروجيني", "stock": 500, "unit": "كجم", "threshold": 50}
    ],
    "networks": [
        {"id": "N1", "name": "مضخة رئيسية", "stock": 2, "unit": "وحدة"},
        {"id": "N2", "name": "فلتر", "stock": 15, "unit": "قطعة"}
    ],
    "logs": [
        {"id": 1700000000000, "date": "2023-11-15", "type": "chemical", "materialId": "C1", "name": "توباس", "sectorId": "S1", "sectorName": "القطاع الشمالي", "qty": 5, "unit": "لتر", "notes": "صرف وقائي"}
    ],
    "users": [
        {"id": 1, "name": "المدير العام", "username": "admin@farm.com", "password": "Mg1996819456", "role": "admin"}
    ]
}

# المتغير الرئيسي الذي سيحمل البيانات في الذاكرة
app_data = initial_data.copy()

# --- 2. دوال الحفظ والتحميل (Persistence Functions) ---

def load_data():
    """تحميل البيانات من ملف JSON."""
    global app_data
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            app_data = json.load(f)
            print("✅ Data loaded successfully from JSON file.")
    except FileNotFoundError:
        print(f"⚠️ Data file '{DATA_FILE}' not found. Using initial data.")
    except json.JSONDecodeError:
        print("❌ Error reading JSON file. Using initial data.")
    except Exception as e:
        print(f"❌ An unexpected error occurred during loading: {e}. Using initial data.")

def save_data():
    """حفظ البيانات الحالية إلى ملف JSON."""
    global app_data
    try:
        # التأكد من أن logs مرتبة زمنياً (الأحدث أولاً)
        app_data["logs"].sort(key=lambda x: x["id"], reverse=True)
        
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(app_data, f, ensure_ascii=False, indent=4)
            return True
    except Exception as e:
        print(f"❌ Error saving data: {e}")
        return False

# --- 3. منطق تسجيل حركة الصرف (Transaction Handler) ---

def handle_transaction(material_type, material_id, sector_id, qty, date, notes=""):
    """
    تسجيل حركة صرف وتحديث المخزون.
    """
    global app_data
    
    try:
        # التحقق من أن الكمية يمكن تحويلها إلى رقم عشري
        qty = float(qty)
    except ValueError:
        return {"success": False, "message": "الكمية المصروفة يجب أن تكون رقماً صالحاً."}

    # تحديد القائمة والتحقق من القيمة
    if material_type == 'chemical':
        material_list = app_data["chemicals"]
    elif material_type == 'network':
        material_list = app_data["networks"]
    else:
        return {"success": False, "message": "نوع المادة غير صالح (يجب أن يكون 'chemical' أو 'network')."}

    # البحث عن المادة والقطاع
    material = next((m for m in material_list if m["id"] == material_id), None)
    sector = next((s for s in app_data["sectors"] if s["id"] == sector_id), None)

    if not material or not sector:
        return {"success": False, "message": "المادة أو القطاع غير موجود."}
    
    if qty <= 0:
        return {"success": False, "message": "يجب أن تكون الكمية أكبر من الصفر."}

    # التحقق من الرصيد
    if material["stock"] < qty:
        return {"success": False, "message": f"الرصيد غير كافٍ. المتوفر: {material['stock']} {material['unit']}."}

    # 1. تحديث المخزون
    material["stock"] = round(material["stock"] - qty, 2) # تقريب الناتج لمنع أخطاء الأرقام العشرية

    # 2. إنشاء سجل حركة جديد
    new_log = {
        "id": int(time.time() * 1000), # توليد ID بالمللي ثانية
        "date": date,
        "type": material_type,
        "materialId": material_id,
        "name": material["name"],
        "sectorId": sector_id,
        "sectorName": sector["name"],
        "qty": qty,
        "unit": material["unit"],
        "notes": notes
    }
    
    # 3. إضافة السجل والحفظ
    app_data["logs"].append(new_log) 
    if save_data():
        return {"success": True, "message": "تم تسجيل الحركة وتحديث المخزون بنجاح."}
    else:
        # التراجع عن تغيير المخزون في حال فشل الحفظ
        material["stock"] = round(material["stock"] + qty, 2)
        return {"success": False, "message": "فشل تسجيل الحركة بسبب خطأ في حفظ البيانات."}


# --- 4. مثال للتنفيذ (يمكن حذفه بعد التجربة) ---

if __name__ == "__main__":
    print("--- بدء نظام المزرعة ---")
    load_data()

    # محاولة صرف ناجحة
    print("\n--- محاولة صرف توباس (5.5 لتر) ---")
    current_stock_c1 = next(m for m in app_data["chemicals"] if m["id"] == "C1")['stock']
    print(f"الرصيد قبل: {current_stock_c1}")
    
    result_ok = handle_transaction(
        material_type="chemical",
        material_id="C1",
        sector_id="S1",
        qty=5.5,
        date=datetime.now().strftime("%Y-%m-%d"),
        notes="صرف وقائي جديد"
    )
    print(f"النتيجة: {result_ok['message']}")
    current_stock_c1 = next(m for m in app_data["chemicals"] if m["id"] == "C1")['stock']
    print(f"الرصيد بعد: {current_stock_c1}")
    
    # محاولة صرف كمية أكبر من الرصيد
    print("\n--- محاولة صرف كمية أكبر من الرصيد (1000 كجم يوريا) ---")
    result_fail = handle_transaction(
        material_type="chemical",
        material_id="C2",
        sector_id="S1",
        qty=1000,
        date=datetime.now().strftime("%Y-%m-%d")
    )
    print(f"النتيجة: {result_fail['message']}")
    
    print("\n--- نهاية التنفيذ ---")
