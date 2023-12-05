import re

with open("in5.txt", "r") as file:
    seeds = [int(x) for x in file.readline().split(":")[1].strip().split(" ")]
    cur_ranges = [(seeds[idx], seeds[idx + 1]) for idx in range(0, len(seeds), 2)]

    is_mapping_mode = False
    mapped_ranges = []
    while line := file.readline():
        is_val_line = line[0].isdigit()
        if not is_mapping_mode and is_val_line:
            is_mapping_mode = True
        if is_mapping_mode:
            if is_val_line:
                dest, source, map_range_len = [int(x) for x in line.strip().split(" ")]
                source_range_end = source + map_range_len - 1

                new_cur_ranges = cur_ranges.copy()
                for idx, (range_start, range_len) in enumerate(cur_ranges):
                    range_end = range_start + range_len - 1

                    # check for general overlap
                    if not range_start <= source <= range_end and not range_start <= source_range_end <= range_end and not (source < range_start and range_end < source_range_end):
                        continue

                    overlap_start = max(source, range_start)
                    overlap_end = min(source_range_end, range_end)
                    # if mapping range overlaps in between
                    if range_start < source:
                        # shorten current range up until overlap begin
                        new_cur_ranges.remove((range_start, range_len))
                        new_cur_ranges.append((range_start, source - range_start))
                    
                    overlap_start_off = overlap_start - source
                    mapped_ranges.append((dest + overlap_start_off, overlap_end - overlap_start + 1))
                    
                    # if overlap ends before original range end
                    if overlap_end < range_end:
                        # add remaining range to (unmapped) current ranges
                        new_cur_ranges.append((overlap_end + 1, range_end - overlap_end))

                    # remove entire unmapped sequence if completely mapped
                    if overlap_start == range_start and overlap_end == range_end:
                        new_cur_ranges.remove((range_start, range_len))
                cur_ranges = new_cur_ranges
            else:
                cur_ranges.extend(mapped_ranges)
                mapped_ranges = []
                is_mapping_mode = False
    cur_ranges.extend(mapped_ranges)
    mapped_ranges = []
    print(sorted(cur_ranges))
    print(min(x for x, y in cur_ranges))
