require "nvchad.mappings"

-- add yours here

local map = vim.keymap.set

map("n", "E", ":lua vim.diagnostic.open_float()<Enter>")
map("n", "<leader>o", ":ObsidianSearch<Enter>")

-- map({ "n", "i", "v" }, "<C-s>", "<cmd> w <cr>")
