#### Create Examples

add_executable(example1 ${CMAKE_CURRENT_SOURCE_DIR}/example.cpp)
target_link_libraries(example1 PRIVATE DimRedTools::DRT)