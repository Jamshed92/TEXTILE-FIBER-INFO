import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Textile Fiber Explorer",
    page_icon="🧵",
    layout="wide",
    initial_sidebar_state="expanded",
)

FIBERS = [
    {
        "Fiber": "Cotton", "Category": "Natural", "Source": "Cotton plant seed hairs",
        "Strength": "Moderate; stronger when wet", "Moisture Absorption": "High",
        "Elasticity": "Low", "Heat Resistance": "Good; can scorch at high heat",
        "Main Uses": "Shirts, denim, towels, bedsheets",
        "Description": "A soft cellulosic fiber that is comfortable, breathable, and absorbent.",
        "Advantages": "Comfortable, absorbent, washable, widely available",
        "Limitations": "Wrinkles easily and may shrink",
    },
    {
        "Fiber": "Flax (Linen)", "Category": "Natural", "Source": "Stem of the flax plant",
        "Strength": "High", "Moisture Absorption": "High",
        "Elasticity": "Low", "Heat Resistance": "Good",
        "Main Uses": "Summer clothing, table linen, furnishing fabrics",
        "Description": "A strong bast fiber known for its cool feel and natural texture.",
        "Advantages": "Strong, absorbent, cool, durable",
        "Limitations": "Wrinkles easily and can be relatively stiff",
    },
    {
        "Fiber": "Jute", "Category": "Natural", "Source": "Stem of the jute plant",
        "Strength": "Good for coarse products", "Moisture Absorption": "Moderate to high",
        "Elasticity": "Low", "Heat Resistance": "Moderate",
        "Main Uses": "Sacks, ropes, carpet backing, geotextiles",
        "Description": "A coarse, lignocellulosic bast fiber commonly used in packaging and technical products.",
        "Advantages": "Renewable, biodegradable, economical",
        "Limitations": "Coarse handle and limited resistance to prolonged moisture exposure",
    },
    {
        "Fiber": "Wool", "Category": "Natural", "Source": "Animal fleece, commonly sheep",
        "Strength": "Moderate", "Moisture Absorption": "High",
        "Elasticity": "High", "Heat Resistance": "Can be damaged by excessive heat",
        "Main Uses": "Sweaters, suits, blankets, carpets",
        "Description": "A protein fiber with natural crimp, warmth, and good resilience.",
        "Advantages": "Warm, resilient, absorbs moisture vapor, naturally flame resistant",
        "Limitations": "May shrink or felt; often needs careful washing",
    },
    {
        "Fiber": "Silk", "Category": "Natural", "Source": "Silkworm cocoon filament",
        "Strength": "Good", "Moisture Absorption": "Good",
        "Elasticity": "Moderate", "Heat Resistance": "Sensitive to high heat",
        "Main Uses": "Fine garments, scarves, ties, luxury textiles",
        "Description": "A fine natural protein filament with a smooth feel and distinctive luster.",
        "Advantages": "Soft, lustrous, fine, good drape",
        "Limitations": "Can be costly and sensitive to sunlight and harsh chemicals",
    },
    {
        "Fiber": "Viscose Rayon", "Category": "Regenerated", "Source": "Regenerated cellulose, usually wood pulp",
        "Strength": "Moderate; lower when wet for conventional viscose", "Moisture Absorption": "High",
        "Elasticity": "Low", "Heat Resistance": "Moderate",
        "Main Uses": "Dresses, linings, shirts, blends",
        "Description": "A manufactured cellulosic fiber that often has a soft feel and good drape.",
        "Advantages": "Soft, absorbent, drapes well, takes dye well",
        "Limitations": "May lose strength when wet and can wrinkle",
    },
    {
        "Fiber": "Lyocell", "Category": "Regenerated", "Source": "Regenerated cellulose",
        "Strength": "Good; generally retains wet strength well", "Moisture Absorption": "High",
        "Elasticity": "Low to moderate", "Heat Resistance": "Moderate",
        "Main Uses": "Apparel, denim, bed linen, nonwovens",
        "Description": "A regenerated cellulosic fiber known for softness and good moisture management.",
        "Advantages": "Soft, absorbent, good drape, often produced using solvent recovery",
        "Limitations": "Can fibrillate under some wet-processing conditions",
    },
    {
        "Fiber": "Polyester", "Category": "Synthetic", "Source": "Petrochemical-based polymer; recycled feedstock is also used",
        "Strength": "Good", "Moisture Absorption": "Low",
        "Elasticity": "Moderate; depends on construction", "Heat Resistance": "Thermoplastic; heat-setting possible",
        "Main Uses": "Sportswear, shirts, fleece, curtains, industrial fabrics",
        "Description": "A widely used synthetic fiber with good durability and quick-drying behavior.",
        "Advantages": "Durable, wrinkle resistant, quick drying, easy care",
        "Limitations": "Low absorbency and may retain oily stains or generate static",
    },
    {
        "Fiber": "Nylon (Polyamide)", "Category": "Synthetic", "Source": "Polyamide polymer",
        "Strength": "High", "Moisture Absorption": "Low to moderate, depending on type",
        "Elasticity": "Good", "Heat Resistance": "Thermoplastic; sensitive to excessive heat",
        "Main Uses": "Sportswear, hosiery, ropes, carpets, airbags",
        "Description": "A strong, abrasion-resistant synthetic fiber with useful flexibility.",
        "Advantages": "Strong, abrasion resistant, lightweight, flexible",
        "Limitations": "Can be heat sensitive and may build up static",
    },
    {
        "Fiber": "Acrylic", "Category": "Synthetic", "Source": "Acrylonitrile-based polymer",
        "Strength": "Moderate", "Moisture Absorption": "Low",
        "Elasticity": "Moderate", "Heat Resistance": "Sensitive to high heat",
        "Main Uses": "Sweaters, blankets, upholstery, outdoor fabrics",
        "Description": "A lightweight synthetic fiber often used as a wool-like alternative.",
        "Advantages": "Lightweight, warm, quick drying, resists moth damage",
        "Limitations": "May pill and can be heat sensitive",
    },
    {
        "Fiber": "Elastane (Spandex)", "Category": "Synthetic", "Source": "Segmented polyurethane",
        "Strength": "Usually used in blends", "Moisture Absorption": "Low",
        "Elasticity": "Very high", "Heat Resistance": "Sensitive to excessive heat",
        "Main Uses": "Stretch denim, leggings, swimwear, sportswear",
        "Description": "A highly extensible manufactured fiber used in small amounts to add stretch.",
        "Advantages": "Excellent stretch and recovery",
        "Limitations": "Can be damaged by excessive heat, chlorine, or harsh care",
    },
    {
        "Fiber": "Hemp", "Category": "Natural", "Source": "Stem of the hemp plant",
        "Strength": "High", "Moisture Absorption": "Good",
        "Elasticity": "Low", "Heat Resistance": "Good under normal textile use",
        "Main Uses": "Blended apparel, canvas, ropes, home textiles",
        "Description": "A bast fiber valued for strength and its potential use in lower-impact textile systems.",
        "Advantages": "Strong, durable, plant-based",
        "Limitations": "Can feel coarse unless processed carefully",
    },
]

df = pd.DataFrame(FIBERS)

st.title("🧵 Textile Fiber Explorer")
st.write("A student-friendly guide to textile fibers, their properties, sources, and applications.")
st.caption("Educational reference: values are general descriptions. Actual performance depends on fiber grade, processing, yarn, fabric construction, and finishing.")

with st.sidebar:
    st.header("Explore fibers")
    search = st.text_input("Search by fiber or use", placeholder="e.g. cotton, sportswear")
    categories = st.multiselect(
        "Fiber category",
        options=["Natural", "Regenerated", "Synthetic"],
        default=["Natural", "Regenerated", "Synthetic"],
    )
    st.divider()
    st.write("**Quick guide**")
    st.markdown("- **Natural:** obtained from plants or animals")
    st.markdown("- **Regenerated:** made by processing natural polymers into fibers")
    st.markdown("- **Synthetic:** made from chemically synthesized polymers")

filtered = df[df["Category"].isin(categories)].copy()
if search.strip():
    term = search.strip().lower()
    searchable = ["Fiber", "Category", "Source", "Main Uses", "Description", "Advantages", "Limitations"]
    mask = filtered[searchable].apply(
        lambda col: col.astype(str).str.lower().str.contains(term, regex=False)
    ).any(axis=1)
    filtered = filtered[mask]

m1, m2, m3 = st.columns(3)
m1.metric("Fibers in library", len(df))
m2.metric("Matching fibers", len(filtered))
m3.metric("Categories", filtered["Category"].nunique() if not filtered.empty else 0)

tab_library, tab_compare, tab_learn = st.tabs(["📚 Fiber Library", "⚖️ Compare Fibers", "🎓 Learn the Basics"])

with tab_library:
    st.subheader("Fiber library")
    if filtered.empty:
        st.info("No fibers match your search. Try another keyword or category.")
    else:
        display_cols = ["Fiber", "Category", "Source", "Strength", "Moisture Absorption", "Elasticity", "Main Uses"]
        st.dataframe(filtered[display_cols], use_container_width=True, hide_index=True)
        selected = st.selectbox("View details for a fiber", filtered["Fiber"].tolist())
        item = filtered[filtered["Fiber"] == selected].iloc[0]
        st.markdown(f"### {item['Fiber']}")
        st.write(item["Description"])
        left, right = st.columns(2)
        with left:
            st.markdown("**Key properties**")
            st.write(f"- Category: {item['Category']}")
            st.write(f"- Source: {item['Source']}")
            st.write(f"- Strength: {item['Strength']}")
            st.write(f"- Moisture absorption: {item['Moisture Absorption']}")
            st.write(f"- Elasticity: {item['Elasticity']}")
            st.write(f"- Heat resistance: {item['Heat Resistance']}")
        with right:
            st.markdown("**Uses and performance**")
            st.write(f"- Main uses: {item['Main Uses']}")
            st.write(f"- Advantages: {item['Advantages']}")
            st.write(f"- Limitations: {item['Limitations']}")
        st.download_button(
            "Download filtered fiber data (CSV)",
            data=filtered.to_csv(index=False).encode("utf-8"),
            file_name="textile_fiber_data.csv",
            mime="text/csv",
        )

with tab_compare:
    st.subheader("Compare two fibers")
    fiber_names = df["Fiber"].tolist()
    c1, c2 = st.columns(2)
    with c1:
        fiber_a = st.selectbox("First fiber", fiber_names, index=0, key="fiber_a")
    with c2:
        fiber_b = st.selectbox("Second fiber", fiber_names, index=7, key="fiber_b")
    a = df[df["Fiber"] == fiber_a].iloc[0]
    b = df[df["Fiber"] == fiber_b].iloc[0]
    compare_fields = [
        "Category", "Source", "Strength", "Moisture Absorption",
        "Elasticity", "Heat Resistance", "Main Uses", "Advantages", "Limitations"
    ]
    comparison = pd.DataFrame({
        "Property": compare_fields,
        fiber_a: [a[field] for field in compare_fields],
        fiber_b: [b[field] for field in compare_fields],
    })
    st.dataframe(comparison, use_container_width=True, hide_index=True)

with tab_learn:
    st.subheader("Textile fiber basics")
    with st.expander("1. What is a textile fiber?"):
        st.write("A textile fiber is a fine, hair-like material with suitable length, flexibility, and strength that can be made into yarn or used in textile products.")
    with st.expander("2. Main fiber groups"):
        st.write("Natural fibers come from plants or animals. Regenerated fibers are made by dissolving and reforming a natural polymer such as cellulose. Synthetic fibers are produced from chemically synthesized polymers.")
    with st.expander("3. Staple and filament fibers"):
        st.write("Staple fibers are short lengths, such as cotton and most wool fibers. Filament fibers are continuous lengths, such as silk and many manufactured fibers.")
    with st.expander("4. Important properties"):
        st.write("Strength helps a fiber resist breaking. Moisture absorption describes how much moisture it can take up. Elasticity describes its ability to stretch and recover. Heat behavior matters during dyeing, finishing, ironing, and use.")
    with st.expander("5. Remember for exams"):
        st.write("Do not judge a fabric only by its fiber name. Yarn structure, fabric construction, blends, dyeing, and finishing also affect the final properties.")

st.divider()
st.caption("Made with Streamlit • Textile Fiber Explorer • For learning purposes, not a substitute for technical datasheets or laboratory testing.")
