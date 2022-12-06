defmodule Day06 do
  def solve(i, x, w) do
    s = i |> Enum.slice(x, w) |> MapSet.new
    if MapSet.size(s) == w, do: x + w, else: solve(i, x + 1, w)
  end
end
