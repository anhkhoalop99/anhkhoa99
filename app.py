from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Platformer 2D", page_icon="🎮", layout="centered")

st.title("🎮 Game Platformer 2D")
st.caption("Nhảy qua hố, đạp đầu slime, nhặt xu và chạm cờ đích để chiến thắng!")

html = (Path(__file__).parent / "game.html").read_text(encoding="utf-8")
components.html(html, height=520, scrolling=False)

with st.expander("Hướng dẫn chơi"):
    st.markdown(
        """
- **← → / A D**: di chuyển
- **Space / ↑ / W**: nhảy (giữ lâu nhảy cao hơn)
- **Shift**: chạy nhanh
- **R**: chơi lại
- Đạp lên đầu slime tím để tiêu diệt, chạm vào cạnh bên là mất mạng.
- Trên điện thoại dùng các nút ◀ ▶ ⤒ bên dưới màn hình game.
        """
    )
