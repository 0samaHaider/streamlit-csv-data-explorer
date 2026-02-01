import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import time

# -------------------- Page Config --------------------
st.set_page_config(page_title="CSV Data Explorer", layout="centered")

# -------------------- App Title --------------------
st.title("📊 CSV Data Explorer")
st.write("Upload a CSV file, explore the data, and visualize columns easily.")

# -------------------- File Uploader --------------------
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

    # -------------------- Data Preview --------------------
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # -------------------- Dataset Summary --------------------
    st.subheader("📋 Dataset Summary")
    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    non_numeric_columns = df.select_dtypes(exclude="number").columns.tolist()
    missing_values = df.isnull().sum()

    st.write(f"**Total Rows:** {df.shape[0]}")
    st.write(f"**Total Columns:** {df.shape[1]}")
    st.write(f"**Numeric Columns ({len(numeric_columns)}):** {numeric_columns}")
    st.write(f"**Non-Numeric Columns ({len(non_numeric_columns)}):** {non_numeric_columns}")
    st.write("**Missing Values per Column:**")
    st.dataframe(missing_values)

    # -------------------- Descriptive Stats --------------------
    st.subheader("📈 Descriptive Statistics (Numeric Columns)")
    if numeric_columns:
        st.dataframe(df[numeric_columns].describe())
    else:
        st.info("No numeric columns found to describe.")

    # -------------------- Column Selectors --------------------
    st.subheader("📌 Select Columns for Visualization")
    all_columns = df.columns.tolist()

    x_column = st.selectbox("Choose X-axis column", all_columns, index=0)
    y_columns = st.multiselect(
        "Choose Y-axis column(s)",
        options=numeric_columns,
        default=numeric_columns[:1] if numeric_columns else []
    )

    # -------------------- Plot Type and Parameters --------------------
    plot_type = st.selectbox(
        "Choose plot type",
        ["Line Chart", "Bar Chart", "Scatter Plot", "Area Chart", "Histogram", "Box Plot"]
    )

    chart_color = st.color_picker("Pick chart color", "#69b3a2")
    chart_width = st.slider("Chart width", 6, 15, 8)
    chart_height = st.slider("Chart height", 4, 10, 5)

    # -------------------- Visualization --------------------
    if not y_columns and plot_type not in ["Histogram", "Box Plot"]:
        st.warning("Please select at least one numeric Y-axis column.")
    elif not y_columns and plot_type in ["Histogram", "Box Plot"]:
        st.warning("Please select at least one numeric column to plot.")
    else:
        with st.spinner("Generating visualization..."):
            time.sleep(0.4)

            fig, ax = plt.subplots(figsize=(chart_width, chart_height))

            if plot_type in ["Line Chart", "Bar Chart", "Scatter Plot", "Area Chart"]:
                for y_col in y_columns:
                    if plot_type == "Line Chart":
                        ax.plot(df[x_column], df[y_col], marker="o", label=y_col, color=chart_color)
                    elif plot_type == "Bar Chart":
                        ax.bar(df[x_column], df[y_col], alpha=0.7, label=y_col, color=chart_color)
                    elif plot_type == "Scatter Plot":
                        ax.scatter(df[x_column], df[y_col], label=y_col, color=chart_color)
                    elif plot_type == "Area Chart":
                        ax.fill_between(df[x_column], df[y_col], alpha=0.3, label=y_col, color=chart_color)
                        ax.plot(df[x_column], df[y_col], color=chart_color)

                ax.set_xlabel(x_column)
                ax.set_ylabel(" / ".join(y_columns))
                ax.set_title(f"{plot_type} of {', '.join(y_columns)} vs {x_column}")
                ax.legend()

            elif plot_type == "Histogram":
                for y_col in y_columns:
                    ax.hist(df[y_col].dropna(), bins=20, alpha=0.7, label=y_col, color=chart_color)
                ax.set_xlabel("Values")
                ax.set_title(f"{plot_type} of {', '.join(y_columns)}")
                ax.legend()

            elif plot_type == "Box Plot":
                # Seaborn expects a dataframe; palette expects list of colors
                sns.boxplot(data=df[y_columns], ax=ax, palette=[chart_color] * len(y_columns))
                ax.set_title(f"{plot_type} of {', '.join(y_columns)}")

            # Prepare PNG buffer BEFORE rendering header row
            buf = io.BytesIO()
            fig.savefig(buf, format="png", bbox_inches="tight")
            buf.seek(0)

            # Put chart + download button in same container (visual "toolbar" feel)
            with st.container(border=True):
                left, right = st.columns([7, 2], vertical_alignment="center")
                with left:
                    st.markdown("### 📈 Visualization")
                with right:
                    st.download_button(
                        label="📥 Download as PNG",
                        data=buf,
                        file_name=f"{plot_type}_chart.png",
                        mime="image/png",
                        use_container_width=True
                    )

                st.pyplot(fig)

else:
    st.info("Please upload a CSV file to get started.")